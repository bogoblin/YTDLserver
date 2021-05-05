from flask import Flask, request, render_template, redirect

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('form.html')


@app.route('/download', methods=['POST'])
def download():
    print(request.form['url'])
    return redirect('/')


if __name__ == '__main__':
    app.run()
