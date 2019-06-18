from flask import current_app as app, jsonify, request
from . import lab
from .handler import get_lab_list_info, get_lab_schedule_info, handler_add_lab_open

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
    usedate = request.values.get('usedate', 0)
    res = get_lab_schedule_info(labid, usedate)
    return jsonify(res)


@lab.route('open')
def add_lab_open():
    post_data = {
        'userid': request.values.get('userid'),
        'content': request.values.get('content'),
        'usernum': request.values.get('usernum'),
        'orderdate': request.values.get('orderdate'),
        'labid':  request.values.get('labid'),
        'guideteacher': request.values.get('guideteacher'),
        'explain': request.values.get('explain'),
        'opentypeid': request.values.get('opentypeid'),
        'expend': request.values.get('expend'),
        'remarks': request.values.get('remarks')
    }
    res = handler_add_lab_open(post_data)
    return jsonify(res)
