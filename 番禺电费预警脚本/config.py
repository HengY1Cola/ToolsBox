# 准备一个数据库连接
userName = 'root'
password = 'root'
host = '127.0.0.1'
port = 3306
database = 'jnu_water'

# 准备邮箱相关配置
# 注明：如果不是QQ邮箱可以到emailTool中把smtp.qq.com修改了
sender = "xxxx@qq.com"  # QQ邮箱
authCode = "xxxx"  # 授权码

aimUrl = "http://127.0.0.1:xxxx/IBSJnuWeb/balance?"  # 自己服务器中的路由

# 使用：
# 1. 填写该服务器数据库的相关信息
# 2. 创建相关数据表格：打开jnuWater.py的注释Base.metadata.create_all(engine)并暂时人工注释该代码下的代码进行运行创建
# 3. 填写邮箱/查询路由的URL（注意拼接是否与你当时的匹配请自己矫正）
# 4. python jnuWater.py -k notice 进行运行
