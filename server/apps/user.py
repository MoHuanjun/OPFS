from flask_login import UserMixin
from werkzeug.security import check_password_hash, generate_password_hash
import pymysql


# 连接数据库
def get_db():
    db = pymysql.connect(host='localhost', user='root', passwd='1234567890', db='userinfo', port=3306, charset='utf8')
    return db


# 查询操作
def search_db():
    db = get_db()
    cur = db.cursor()
    sql = "select * from userinfo.users"
    cur.execute(sql)
    user_info = cur.fetchall()
    # print(u'查询到的数据', user_info)
    cur.close()
    db.close()
    return user_info


# 查找数据库中内容
user = search_db()


def data_of_users(user_list):
    data = []
    for row in user_list:
        dic = {'Uid': row[0], 'name': row[1], 'password': generate_password_hash(row[2])}
        data.append(dic)
        print(data)
    return data


USERS = data_of_users(user)


class User(UserMixin):
    def __init__(self, accounts):
        self.username = accounts.get("name")
        self.password_hash = accounts.get("password")
        self.id = accounts.get("id")

    @staticmethod
    def queryUser(username):
        for accounts in USERS:
            if accounts.get('name') == username:
                return User(accounts)
        return None

    def verifyPassword(self, password):
        if self.password_hash is None:
            return False
        return check_password_hash(self.password_hash, password)

    def get_id(self):
        return self.id

    def get(self):
        if not self:
            return None
        for accounts in USERS:
            if str(accounts.get('id')) == str(self):
                return User(accounts)
        print('None')
        return None
