from flask import Flask
from flask import render_template
from flask import request
from flask import url_for
from flask import jsonify # For AJAX transactions

from pymongo import MongoClient # DB client
import CONFIG
import random
import logging
import json

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

## FUNCTIONS / ACTIONS ##
@app.route('/_wait_time')
def wait_time():
	rando = random.randrange(5, 50)
	return jsonify(result = str(rando))




if __name__ == "__main__":
    # App is created above so that it will
    # exist whether this is 'main' or not
    app.debug=CONFIG.DEBUG
    app.logger.setLevel(logging.DEBUG)
    # We run on localhost only if debugging,
    # otherwise accessible to world
    if CONFIG.DEBUG:
        # Reachable only from the same computer
        app.run(port=CONFIG.PORT)
    else:
        # Reachable from anywhere 
        app.run(port=CONFIG.PORT,host="0.0.0.0")