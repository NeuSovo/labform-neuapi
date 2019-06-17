import os

env_prefix = 'NEU_'
# global config
HOST = '127.0.0.1' or os.getenv(env_prefix + 'HOST')
PORT = '5000' or os.getenv(env_prefix + 'PORT')

BASE_URL = 'http://172.17.4.12:9210/odc/' or os.getenv(env_prefix + 'BASE_URL')
CONSID = 'LMS' or os.getenv(env_prefix + 'CONSID')
ACCESSKEY = 'lms123' or os.getenv(env_prefix + 'ACCESSKEY')

# api list
LOGIN_API = 'api/auth/user/v1/preauthlogin.do'