from flask import Flask
from flask import render_template
from flask import request
from flask import url_for

app = Flask(__name__)

@app.route('/')
@app.route('/home')
@app.route('/index')
def home():
  return render_template('index.html')

@app.route('/hello')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    app.run()