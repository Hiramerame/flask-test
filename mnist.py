import os
from flask import Flask, request, redirect, render_template, flash
from werkzeug.utils import secure_filename
import numpy as np


classes = ["0","1","2","3","4","5","6","7","8","9"]
image_size = 28

UPLOAD_FOLDER = "./static/images"
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('ファイルがありません')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('ファイルがありません')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(UPLOAD_FOLDER, "input.png"))
            filepath = os.path.join(UPLOAD_FOLDER, filename)
            
            

            return render_template("index.html", answer=filepath, path_input_img=filepath)

    return render_template("index.html",answer="")

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 8080))
    app.run(host ='0.0.0.0',port = port)