from flask import Flask, request, render_template, send_file
import qrcode
from io import BytesIO

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate_qr():
    text = request.form.get('text')
    if not text:
        return 'Missing text', 400

    img = qrcode.make(text)
    buffer = BytesIO()
    img.save(buffer)
    buffer.seek(0)
    
    return send_file(buffer, mimetype='image/png')

if __name__ == '__main__':
    app.run(debug=True)
