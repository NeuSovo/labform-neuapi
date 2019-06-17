import hashlib

def sign_md5(sign_raw):
    sign_md5 = hashlib.md5()
    sign_md5.update(sign_raw.encode(encoding='utf-8'))
    sign = sign_md5.hexdigest()
    print('sign_md5:' + sign)
    return sign
