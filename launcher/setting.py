# -*- encoding=utf8 -*-

# 导入os
import os

# 调试模式是否开启
DEBUG = True

# 数据库更改通知设置为关闭
SQLALCHEMY_TRACK_MODIFICATIONS = False

# session 必须需要设置的key
SECRET_KEY = os.urandom(24)

# 不要使用ASCII码展示,解决中文乱码问题
JSON_AS_ASCII = False

# 数据库类型
DIALECT = 'mysql'
# 数据库连接驱动
DRIVER = 'mysqlconnector'
# 数据库用户名
USERNAME = 'root'
# 数据库密码
PASSWORD = ''
# 数据库地址
HOST = '127.0.0.1'
# 数据库端口
PORT = '3306'
# 数据库名称
DB = 'launcher'
# mysql数据库连接
# ,数据库URI（dialect + driver://username:password@host:port/database?charset）
SQLALCHEMY_DATABASE_URI = '%s+%s://%s:%s@%s:%s/%s?charset=utf8' \
                          % (DIALECT, DRIVER, USERNAME, PASSWORD, HOST, PORT, DB)
