# !/usr/bin/evn python3
# -8- encoding=utf8 -8*

from launcher import app
import os
# 导入蓝图类
from launcher.launcher_api import blue_launcher

# 访问地址
host = '192.168.101.105'
# 端口号
port = 8080
# 常用的请求模式组合
request_methods = ['GET', 'POST']

# 文件的根目录, __file__ refers to the file settings.py
APP_ROOT = os.path.dirname(os.path.abspath(__file__))
# 静态json文件存放的具体路径
APP_STATIC_JSON = os.path.join(APP_ROOT, 'launcher/static/json')

# 注册模块蓝图,饼指定url 前缀
app.register_blueprint(blue_launcher, url_prefix='/launcher')


@app.route('/index', methods=request_methods)
def index():
    path = os.path.join(APP_STATIC_JSON, 'featured.txt')
    print(path)
    with open(path, 'r') as f:
        result = f.read()
    return result.encode()


if __name__ == '__main__':
    app.run(host=host, port=port)
