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

@app.route('/admin')
def admin_page():
	return render_template('admin.html')

@app.route('/waitlist')
def waitlist():
	return render_template('waitlist.html')

@app.route('/test')
def nav_bar():
	return render_template('base-template.html')

@app.route('/hello')
def hello_world():
  return 'Hello World!'

if __name__ == '__main__':
  app.run()