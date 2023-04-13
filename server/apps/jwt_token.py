import jwt
from jwt import PyJWTError
from datetime import datetime, timedelta

SECRET_KEY = b'\x92R!\x8e\xc6\x9c\xb3\x89#\xa6\x0c\xcb\xf6\xcb\xd7\xbc'


def genToken(data):
    expInt = datetime.utcnow() + timedelta(seconds=60)
    payload = {
      'exp': expInt,
      'data': data
    }
    token = jwt.encode(payload, key=SECRET_KEY, algorithm='HS256')
    return token


def verifyToken(tokenStr):
    try:
        payload = jwt.decode(tokenStr, key=SECRET_KEY, algorithms=['HS256'])
        return payload
    except PyJWTError as e:
        print("jwt验证失败: %s" % e)
    return None
