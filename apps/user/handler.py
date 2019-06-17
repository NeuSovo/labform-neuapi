import time
import random

from flask import current_app as app

from utils.tools import sign_md5


def do_the_login(username, password, callback):
    request_url = app.config['BASE_URL'] + app.config['LOGIN_API']
    consid = app.config['CONSID']
    accesskey = app.config['ACCESSKEY']
    timestamp = str(int(time.time()))
    rand = str(random.randint(100000, 999999))
    sign = sign_md5(accesskey + timestamp + rand)
    post_data = {

    }
    print (request_url, sign)
    # res = requests.post(url=request_url, data=post_data)
