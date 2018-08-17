# !/usr/bin/evn python3
# -8- encoding=utf8 -8*

from launcher import app
# 导入蓝图类
from launcher.launcher_api import blue_launcher

# 访问地址
host = '192.168.101.105'
# 端口号
port = 8080


# 注册模块蓝图,饼指定url 前缀
app.register_blueprint(blue_launcher, url_prefix='/launcher')


if __name__ == '__main__':
    app.run(host=host, port=port)
