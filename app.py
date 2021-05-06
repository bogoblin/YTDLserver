import os

from flask import Flask, request, render_template
from flask_cors import CORS
import youtube_dl

app = Flask(__name__)
CORS(app)


download_dir = r'D:\YouTube'


ydl_opts = {
    'outtmpl': os.path.join(download_dir, "%(uploader)s", "%(title)s.%(ext)s"),
    'noplaylist': True
}


@app.route('/')
def home():
    return render_template('form.html')


@app.route('/download', methods=['POST'])
def download():
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        url = request.form['url']

        info = ydl.extract_info(url, download=False, process=False)

        # Only download if it's a single video, not a channel or a playlist
        if info['webpage_url_basename'] == 'watch':
            ydl.download([url])
    return "Download complete", 200


if __name__ == '__main__':
    app.run()
