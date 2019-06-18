from flask import current_app as app, jsonify, request
from . import user
import config

from .handler import do_the_login, get_user_info, send_user_info

@user.route('/login', methods=['GET', 'POST'])
def neu_login():
    userid = request.values.get('userid')
    userpwd = request.values.get('userpwd')
    callback = request.values.get('callback')
    if not userid or not userpwd or not callback:
        return jsonify({'msg': 'param error'}), 400
    res = do_the_login(userid, userpwd, callback)
    return jsonify(res)


@user.route('/info')
def user_info():
    consuserid = request.values.get('consuserid')
    if not consuserid:
        return jsonify({'msg': 'error'})
    res = get_user_info(consuserid)
    user_info = res['userinfo']
    send_res = send_user_info(user_info)
    print (send_res)
    return jsonify(user_info)


@user.route('/callback')
def test_callback():
    return jsonify(request.values)
