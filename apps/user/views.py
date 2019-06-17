from flask import current_app as app
from . import user
import config

from .handler import do_the_login

@user.route('/login')
def neu_login():
    do_the_login('d','d','d')
    return str({"123":'2'})

@user.route('/info/<str:user_id>')
def get_user_info(user_id):
    return user_id


