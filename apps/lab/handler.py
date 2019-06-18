import time
import random
import requests
from flask import current_app as app
from utils.tools import sign_md5


def get_lab_list_info(labid=None, labtypeid=None):
    request_url = app.config['BASE_URL'] + app.config['LAB_LIST_API']
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
    }
    if labid:
        post_data['labid'] = labid
    if labtypeid:
        post_data['labtypeid'] = labtypeid 

    res = requests.post(url=request_url, data=post_data)
    return res.json()


def get_lab_schedule_info(labid):
    request_url = app.config['BASE_URL'] + app.config['LAB_SCHEDULE_LIST_API']
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
    }
    if labid:
        post_data['labid'] = labid

    res = requests.post(url=request_url, data=post_data)
    print (res.text)
    return res.json()