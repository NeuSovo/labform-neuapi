from flask import current_app as app, jsonify, request
from . import lab
from .handler import get_lab_list_info, get_lab_schedule_info

"""
type id
[1 公共基础] 
[2 专业基础] 
[7 信息商务] 
[4 计算机] 
[8 商务管理] 
[21 电子工程] 
[41 数字艺术] 
[42 外语]
"""

@lab.route('list')
def query_lab_list():
    labtypeid  = request.values.get('labtypeid', 0)
    labid = request.values.get('labid', 0)
    res = get_lab_list_info(labid, labtypeid)
    return jsonify(res)

@lab.route('schedule')
def query_lab_schedule_list():
    labid = request.values.get('labid', 0)
    res = get_lab_schedule_info(labid)
    return jsonify(res)


