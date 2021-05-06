import os

from flask import Flask, request, render_template, redirect
import youtube_dl

app = Flask(__name__)


class MyLogger(object):
    def debug(self, msg):
        print('debug - '+msg)

    def warning(self, msg):
        print('warning - '+msg)

    def error(self, msg):
        print('error - '+msg)


download_dir = r'D:\YouTube'


def hook(d):
    print(d)


ydl_opts = {
    'outtmpl': os.path.join(download_dir, "%(uploader)s", "%(title)s.%(ext)s"),
    'progress_hooks': [hook]
}


@app.route('/')
def home():
    return render_template('form.html')


@app.route('/download', methods=['POST'])
def download():
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([request.form['url']])
    return redirect('/')


if __name__ == '__main__':
    app.run()
