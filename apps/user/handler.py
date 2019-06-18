import time
import random
import requests
from flask import current_app as app
from lxml import etree
from utils.tools import sign_md5


def do_the_login(userid, userpwd, callback):
    request_url = app.config['BASE_URL'] + app.config['LOGIN_API']
    consid = app.config['CONSID']
    accesskey = app.config['ACCESSKEY']
    timestamp = str(int(time.time()))
    rand = str(random.randint(100000, 999999))
    sign = sign_md5(accesskey + timestamp + rand)
    post_data = {
        'consid': consid,
        'timestamp': timestamp,
        'rand': rand,
        'sign': sign,
        'callback': callback,
        'userid': userid,
        'userpwd': userpwd
    }
    res = requests.post(url=request_url, data=post_data)
    
    # 非第一次登录 且登录成功， 且回调请求成功
    if res.headers.get('Content-Type') == 'application/json':
        return res.json()
    
    # 第一次登录，confirm 界面 拿到 sign 请求确认
    # [in] faster re and str.find
    if '申请获取您的信息' in res.text:
        selectot = etree.HTML(res.text)
        name = selectot.xpath('//div[@class="example"]/div/div/h4//text()')
        print("first login ===>", name[0])
        action = selectot.xpath('//form[@id="loginfm"]/@action')
        sign = selectot.xpath('//form[@id="loginfm"]/input[@name="sign"]/@value')
        post_data['sign'] = sign[0]
        confirm_url = app.config['BASE_URL'] + action[0]
        res = requests.post(url=confirm_url, data=post_data)
    
        if res.headers.get('Content-Type') == 'application/json':
            return res.json()
        else:
            print (res.text)
            return {'msg': 'failed'}

    # 登录失败，一般指密码错误
    return {'msg':'failed'}


def get_user_info(consuserid):
    request_url = app.config['BASE_URL'] + app.config['GET_USERINFO_API']
    consid = app.config['CONSID']
    accesskey = app.config['ACCESSKEY']
    timestamp = str(int(time.time()))
    rand = str(random.randint(100000, 999999))
    sign = sign_md5(accesskey + timestamp + consuserid + rand)
    post_data = {
        'consid': consid,
        'timestamp': timestamp,
        'rand': rand,
        'sign': sign,
        'consuserid': consuserid
    }
    print(request_url, post_data)
    res = requests.post(url=request_url, data=post_data)
    return res.json()
