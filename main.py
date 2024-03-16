from flask import Flask, render_template, request, redirect, url_for, send_file
from rembg import remove
from io import BytesIO

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'image' not in request.files:
        return redirect(request.url)
    image = request.files['image']
    if image.filename == '':
        return redirect(request.url)
    if image:
        image_data = image.read()
        # Remove background
        output_image_data = remove(image_data)
        # Send the processed image as a response
        return send_file(BytesIO(output_image_data), mimetype='image/png')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5100)
