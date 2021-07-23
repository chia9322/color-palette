from PIL import Image
from color_manager import find_top_colors
from flask import Flask, render_template, redirect, url_for, request
from werkzeug.exceptions import BadRequestKeyError
import os

UPLOAD_FOLDER = 'static/images'

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
app.config["IMAGE_UPLOADS"] = UPLOAD_FOLDER


@app.route('/', methods=['GET', 'POST'])
def home():
    try:
        if request.args['img']:
            img = request.args['img']
            image_url = f'{UPLOAD_FOLDER}/{img}'
    except BadRequestKeyError:
        image_url = f'{UPLOAD_FOLDER}/default.jpg'
    image = Image.open(image_url)
    colors = find_top_colors(image)
    return render_template('index.html', image=image_url, colors=colors)

@app.route('/upload-image', methods=['GET', 'POST'])
def upload_image():
    if request.method == "POST":
        try:
            if request.files:
                image = request.files["image"]
                img = image.filename
                img_format = img.split('.')[1]
                image.save(os.path.join(app.config["IMAGE_UPLOADS"], f'upload-img.{img_format}'))
                return redirect(url_for('home', img=f'upload-img.{img_format}'))
        except:
            return redirect(url_for('home'))
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True)