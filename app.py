import os

from flask import Flask, request, render_template
from flask_cors import CORS
import youtube_dl

app = Flask(__name__)
CORS(app)


download_dir = r'D:\YouTube'


ydl_opts = {
    'outtmpl': os.path.join(download_dir, "%(uploader)s", "%(title)s.%(ext)s")
}


@app.route('/')
def home():
    return render_template('form.html')


@app.route('/download', methods=['POST'])
def download():
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([request.form['url']])
    return "Download complete", 200


if __name__ == '__main__':
    app.run()
