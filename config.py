import os

env_prefix = 'NEU_'
# global config
HOST = '127.0.0.1' or os.getenv(env_prefix + 'HOST')
PORT = '5000' or os.getenv(env_prefix + 'PORT')

BASE_URL = 'http://127.0.0.1:9210' or os.getenv(env_prefix + 'BASE_URL')
CONSID = 'sss' or os.getenv(env_prefix + 'CONSID')
ACCESSKEY = 'sss' or os.getenv(env_prefix + 'ACCESSKEY')

# api list
# user
LOGIN_API = '/odc/api/auth/user/v1/authlogin.do'
GET_USERINFO_API =  '/odc/api/auth/user/v1/get_user_info_by_consuserid.do'

# lab
LAB_LIST_API = '/odc/api/lms/lab/v1/query_lms_lab_list.do'
LAB_SCHEDULE_LIST_API = '/odc/api/lms/lab/v1/query_lms_lab_schedule_list.do'