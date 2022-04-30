import os.path
import time
from datetime import datetime, date
import logging
import argparse
from concurrent.futures import ThreadPoolExecutor, as_completed
import requests
from sqlalchemy import create_engine, Column, Integer, String, DateTime, and_, delete
from sqlalchemy.orm import declarative_base, Session
from emailTool import send, readHtml
from config import *

# 声明一个数据库引擎
engine = create_engine(
    f'mysql+mysqlconnector://{userName}:{password}@{host}:{port}/{database}?auth_plugin=mysql_native_password',
    future=True)

# 声明ORM的一个基类并建立映射关系
Base = declarative_base()


class emailNotice(Base):
    """邮件通知表格"""
    __tablename__ = 'email_notice'
    id = Column(Integer, name='id', primary_key=True)
    email = Column(String(64), nullable=False, name='email', comment="注册邮箱")
    dormitory = Column(String(64), nullable=False, name='dormitory', comment="绑定宿舍")
    ip = Column(String(64), nullable=False, name='ip', comment="注册Ip")
    create_at = Column(DateTime, name='create_at', comment="创建时间")
    update_at = Column(DateTime, name='update_at', comment="更新时间")
    is_verify = Column(Integer, name='is_verify', default=0, comment="是否通过邮箱验证")
    is_work = Column(Integer, name='is_work', default=1, comment='是否仍然生效')


# Base.metadata.create_all(engine)  # 解除该注释即可以创建对应的数据表格

# todo 查询有效用户
def findWhoCouldUseIt():  # is_verify且任然在is_work
    session = Session(bind=engine, future=True)
    info = session.query(emailNotice).filter(and_(emailNotice.is_verify == 1, emailNotice.is_work == 1)).all()
    return info


# todo 查询余额
def getBalance(infoList) -> list:
    needList = []
    executor = ThreadPoolExecutor(max_workers=5)
    allTask = [executor.submit(netWay, each) for each in infoList]
    for future in as_completed(allTask):  # 获取到已经完成的了
        flag, email = future.result()
        if flag:
            needList.append(email)
    return needList


def netWay(eachInfo):
    try:
        email, dormitoryNum = eachInfo
        res = requests.get(aimUrl + f"dormitory={dormitoryNum}", timeout=30, verify=False).json()
        balance = res['data']['balance']
        if int(balance) < 30:
            return True, email
        return False, -1
    except Exception as e:
        logger.info('Error Occurred : %s', e)
        return False, -1


# todo 处理群发
def queueSend(needNoticeList):
    resList = []
    for x in range(0, len(needNoticeList), 20):
        resList.append(needNoticeList[x: x + 20])
    return resList


# todo 查询接口并通知对应的用户
def noticeUser():
    try:
        # todo 找到需要通知的
        resMaps = findWhoCouldUseIt()
        if list(resMaps) == 0:
            logging.info("查询到0个用户")
            return
        baseInfoList = [(each.email, each.dormitory) for each in resMaps]
        needNoticeList = getBalance(baseInfoList)
        # todo 发送通知
        subject = '宿舍电费预警通知(勿回)'
        needNoticeList = queueSend(needNoticeList)
        body = readHtml(os.path.join(templatePath, "warning.html"))
        for each in needNoticeList:
            logging.info(f"查询：{str(each)}")
            time.sleep(10)  # 休息10秒钟 即使群发但是只要高频率调用QQ第三方服务会拒绝
            send(subject, body, each)
        # todo 通知管理者
        send(f"[*] 查询成功", f"时间：{timeNow}， 通知了：{str(needNoticeList)}", sender)
    except Exception as e:
        send(f"[*] 查询失败", f"时间：{timeNow}， {e}", sender)
        logger.error('Error Occurred : %s', e)


# todo 删除每日失效用户（平时不使用）
def deleteUser():
    try:
        session = Session(bind=engine, future=True)
        stmt = delete(emailNotice).where(emailNotice.is_verify == 0)
        resInfo = session.execute(stmt)
        session.commit()
        logging.info(f"删除了：{resInfo.rowcount}条")
    except Exception as e:
        send(f"[*] 删除每日失效用户失败", f"时间：{timeNow}， {e}", sender)
        logger.error('Error Occurred : %s', e)


# todo 通知所有人消息（平时不使用）
def radioNotice():
    try:
        session = Session(bind=engine, future=True)
        info = session.query(emailNotice).filter(and_(emailNotice.is_verify == 1, emailNotice.is_work == 1)).all()
        allUser = [x.email for x in info]
        allUser = queueSend(allUser)
        subject = '新一年预警服务开启'
        body = readHtml(os.path.join(templatePath, "notice.html"))
        for x in allUser:
            logging.info(f"查询：{str(x)}")
            send(subject, body, x)
    except Exception as e:
        logger.error('Error Occurred : %s', e)


if __name__ == "__main__":
    # todo 设置路径
    currentPath = str.rsplit(__file__, '/', 1)[0].replace("jnuWater.py", "")
    logPath = os.path.join(currentPath, "log")
    fileName = os.path.join(logPath, date.today().strftime("%Y_%m") + ".log")
    timeNow = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    templatePath = os.path.join(currentPath, "template")
    # todo 设置日志
    logging.basicConfig(level=logging.INFO,
                        filename=fileName,
                        datefmt='%Y/%m/%d %H:%M:%S',
                        format='%(asctime)s - %(name)s - %(levelname)s - %(lineno)d - %(module)s - %(message)s')
    logger = logging.getLogger(__name__)
    # todo 任务
    parser = argparse.ArgumentParser(
        description='Water warning system by Python.',
        formatter_class=argparse.RawTextHelpFormatter
    )
    parser.add_argument(
        '-k',
        '--key',
        required=False,
        type=str,
        help='Keywords to be present in the title'
    )
    args = parser.parse_args()
    if args.key == 'delete':
        deleteUser()  # 删除每日失效用户
    elif args.key == 'notice':
        noticeUser()  # 查询接口并通知对应的用户
    else:
        logging.info("参数解析错误")
    # radioNotice()  # 通知所有人消息
