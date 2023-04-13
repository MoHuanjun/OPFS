from flask import Flask
from flask_cors import CORS
# 引入login.py模块
from login import login_page
from upload import uploader


app = Flask(__name__)
app.secret_key =b'\x15f\x07\xd3\xd9\xbf*\x82\xd1\xe6\xb4\xf2\x95\xdd\x8f\x12'
# 命令行中运行后拷贝出随机值  python -c "import os; print(os.urandom(16))"

app.register_blueprint(login_page, url_prefix='/')
app.register_blueprint(uploader, url_prefix='/uploader')
app.config.from_object(__name__)
# 启动CORS
CORS(app, resources=r'/*')


if __name__ == '__main__':
    app.run(debug=True)
