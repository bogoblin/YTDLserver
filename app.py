from flask import Flask, request, render_template, redirect
import youtube_dl

app = Flask(__name__)


class MyLogger(object):
    def debug(self, msg):
        print(msg)

    def warning(self, msg):
        print(msg)

    def error(self, msg):
        print(msg)


ydl_opts = {
    'logger': MyLogger()
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
