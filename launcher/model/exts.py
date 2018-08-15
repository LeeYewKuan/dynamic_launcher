# !usr/bin/env python3
# -*- encoding=utf8 -*-

# 此模块为了解决db循环引用做的中间类
# 导入 SQLAlchemy
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
