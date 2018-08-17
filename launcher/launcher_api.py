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
# 导入os类
import os
# 导入flask请求对象，获取请求的参数
from flask import request
# 导入json
import json

# 设置蓝图别名
blue_launcher = Blueprint('launcher', __name__)

# 常用的请求模式组合
request_methods = ['GET', 'POST']

# 文件的根目录, __file__ refers to the file settings.py
APP_ROOT = os.path.dirname(os.path.abspath(__file__))
# 静态json文件存放的具体路径
APP_STATIC_JSON = os.path.join(APP_ROOT, 'static/json')


@blue_launcher.route("/navigation_list", methods=request_methods)
def get_navigation_list():
    nav_list = Navigation.query.filter().all()
    data_list = []
    for item in nav_list:
        result = item.to_json()
        result.pop('id')
        data_list.append(result)
    task = {
        "ret": "0",
        "message": "成功",
        "data": data_list
    }
    return jsonify(task), 200


@blue_launcher.route("/app_config", methods=request_methods)
def app_config():
    task = {
        "ret": "0",
        "message": "成功",
        "data": {
            "logo": "http://pdi6uq9ul.bkt.clouddn.com/logo.png"
        }
    }
    return jsonify(task), 200


@blue_launcher.route("/get_panel", methods=request_methods)
def get_panel():
    str_params = str(request.get_data(), encoding='utf-8')
    print(str_params)
    panel_id = str_params.split("=")[1]
    print(panel_id)
    file_name = 'featured_%s.txt' % 1001
    path = os.path.join(APP_STATIC_JSON, file_name)
    print(path)
    with open(path, 'r') as f:
        result = f.read()
    return result.encode(), 200
