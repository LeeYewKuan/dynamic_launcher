# !usr/bin/env python3
# -*- encoding=utf8 -*-

# launcher相关路由配置

# 导入蓝图类
from flask.blueprints import Blueprint
# 导入数据库
from launcher.model.models import db
# 导入需要的module
from launcher.model.models import Navigation
# 导入json 工具类
from flask import jsonify

# 设置蓝图别名
blue_launcher = Blueprint('launcher', __name__)


@blue_launcher.route("/navigation_list", methods=["GET", "POST"])
def get_navigation_list():
    nav_list = Navigation.query.filter().all()
    data_list = []
    for item in nav_list:
        result = item.to_json()
        result.pop('id')
        data_list.append(result)

    print(nav_list)
    print(type(nav_list))
    task = {
        "ret": "0",
        "message": "成功",
        "data": data_list
    }
    return jsonify(task), 200


@blue_launcher.route("/app_config", methods=["GET", "POST"])
def app_config():
    task = {
        "ret": "0",
        "message": "成功",
        "link": "http://pdi6uq9ul.bkt.clouddn.com/logo.png"
    }
    return jsonify(task), 200

