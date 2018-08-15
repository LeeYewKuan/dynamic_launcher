# !usr/bin/evn python3
# -*- encoding=utf8 -*-

# 导入flask框架
from flask import Flask
# 导入应用配置文件
from launcher import setting
# 导入映射关系管数据库模块
from launcher.model.exts import db
# 导入实体类
from launcher.model.models import Navigation


# 创建对象
app = Flask(__name__)
# 经应用配置文件导入到app中
app.config.from_object(setting)

# 初始化db
db.init_app(app)
db.create_all(app=app)




