import json
from flask import Blueprint, request
from flask_login import LoginManager, login_user
from user import User
from jwt_token import genToken, verifyToken

login_page = Blueprint('login_page', __name__)

login_manager = LoginManager()
login_manager.login_view = 'helloworld'


@login_page.record_once
def on_load(state):
    login_manager.init_app(state.app)


@login_manager.request_loader
def load_user_from_request(requests):
    token = requests.headers.get('Authorization')
    if token is None:
        return None

    payload = verifyToken(token)
    if payload is not None:
        user = User.queryUser(payload['data']['username'])
    else:
        user = None
    return user


@login_page.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.queryUser(username)

    if (user is not None) and (user.verifyPassword(password)):
        login_user(user)
        token = genToken({'username': username, 'password': '******'})
        returnData = {'code': 0, 'msg': 'success', 'data': {'token': token}}
        return json.dumps(returnData), 200
    else:
        returnData = {'code': 1, 'msg': 'success', 'data': 'username or password is not correct'}
        return json.dumps(returnData), 100
