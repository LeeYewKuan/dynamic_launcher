# !usr/bin/env python3
# -*- encoding=utf8 -*-

# 导入数据库管理类 db
from launcher.model.exts import db


# 当行类,下发导航的分类列表
class Navigation(db.Model):
    # 数据库存储的表名
    __tablename__ = 'navigation'
    # 数据库自增的字段
    id = db.Column(db.Integer, primary_key=True)
    # 导航的真实ID
    navigation_id = db.Column(db.String(16), unique=True, nullable=False)
    # 导航的名称
    navigation_name = db.Column(db.String(32), nullable=False)
    # 是否聚焦，默认给值不聚焦
    flag_focus = db.Column(db.String(8), nullable=False, default="0")

    # 初始化赋值
    def __init__(self, navigation_id, navigation_name, flag_focus):
        self.navigation_id = navigation_id
        self.navigation_name = navigation_name
        self.flag_focus = flag_focus

    # 对象序列化方法
    def __repr__(self):
        return '<Navigation %r,%r,%r>' % (self.navigation_id, self.navigation_name, self.flag_focus)

    # 将对象专为字符串
    def to_json(self):
        dict_item = self.__dict__
        if "_sa_instance_state" in dict_item:
            del dict_item["_sa_instance_state"]
        return dict_item



