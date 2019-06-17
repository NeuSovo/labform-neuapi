# -*- encoding: utf-8 -*-
from flask import Blueprint
from flask import current_app as app
# 实例化 Blueprint 类，两个参数分别为蓝本的名字和蓝本所在包或模块，第二个通常填 __name__ 即可
user = Blueprint('user', __name__)

from . import views