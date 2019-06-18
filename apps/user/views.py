from flask import current_app as app, jsonify, request
from . import user
import config

from .handler import do_the_login, get_user_info

@user.route('/login', methods=['GET', 'POST'])
def neu_login():
    userid = request.values.get('userid')
    userpwd = request.values.get('userpwd')
    callback = request.values.get('callback')
    if not userid or not userpwd or not callback:
        return jsonify({'msg': 'param error'}), 400
    res = do_the_login(userid, userpwd, callback)
    return jsonify(res)


@user.route('/info/<user_id>')
def user_info(user_id):
    res = get_user_info(user_id)
    return jsonify(res)


@user.route('/callback')
def test_callback():
    return jsonify(request.values)
