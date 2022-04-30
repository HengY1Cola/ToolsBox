# -*- coding:utf-8 -*-
import smtplib
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from config import *


def content(file_path):
    with open(file_path, encoding='utf-8') as f:
        return f.read()


def send(subject, text, email):
    Subject = subject
    receivers = email  # 收件人邮箱
    receivers = ','.join(receivers) if isinstance(receivers, list) else receivers

    message = MIMEMultipart('related')
    message['Subject'] = Subject
    message['From'] = '%s  <%s>' % (Header('HengY1Service', 'utf-8'), sender)
    contentInfo = MIMEText(text, _subtype='html', _charset='UTF-8')
    message.attach(contentInfo)
    try:
        server = smtplib.SMTP_SSL("smtp.qq.com", 465)
        server.login(sender, authCode)  # 授权码
        server.sendmail(sender, receivers.split(','), message.as_string())
        server.quit()
    except Exception as e:
        print('邮件发送异常, ', str(e))


def readHtml(path):
    return content(path)


if __name__ == "__main__":
    # 测试邮件发送
    send('宿舍电费预警通知(勿回)', '<h1>自定义HTML超文本部分<h1>', ['xxx@qq.com', 'xxx@qq.com'])
