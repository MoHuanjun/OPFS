import os
from flask import Blueprint, request
from werkzeug.utils import secure_filename

uploader = Blueprint('upload', __name__)

# 上传文件保存的路径
UPLOAD_FOLDER = './'


@uploader.route('/uploader', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        # 保存文件
        f.save(os.path.join(UPLOAD_FOLDER, secure_filename(f.filename)))
        return 'file uploaded successfully'
