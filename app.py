import flask
from flask import render_template
from flask import request
from flask import url_for
from flask import redirect
from flask import jsonify # For AJAX transactions

import uuid
import arrow
import random
import logging
import json

# Mongo database
from pymongo import MongoClient
import CONFIG
try: 
    dbclient = MongoClient(CONFIG.MONGO_URL)
    db = dbclient.greathost
    signinCollection = db.signins
    tableCollection = db.tables
    notificationCollection = db.notifications

except:
    print("Failure opening database.  Is Mongo running? Correct password?")
    sys.exit(1)


app = flask.Flask(__name__)

@app.route('/')
@app.route('/home')
@app.route('/index')
def home():
  return render_template('index.html')

@app.route('/waitlist')
def waitlist():
  app.logger.debug("Waitlist...")
  all_signins = get_signins()
  waitlist = [ ]
  seated = [ ]
  for signin in all_signins:
      app.logger.debug("Signin: " + str(signin))
      if signin['seat_time'] == "False" and signin['leave_time'] == "False":
        waitlist.append(signin)
      elif signin['leave_time'] == "False":
        seated.append(signin)

  flask.session['waitlist'] = waitlist
  flask.session['seated'] = seated
  return render_template('waitlist.html')

@app.route('/test')
def nav_bar():
  return render_template('base-template.html')

@app.route('/admin')
@app.route('/admin/')
@app.route('/admin/overview')
def admin_page():
  return render_template('admin-overview.html')

@app.route('/admin/tables')
def table_inventory():
  flask.session['tables'] = get_tables()
  return render_template('admin-tables.html')

@app.route('/admin/tables/add')
def table_add_page():
  return render_template('admin-add-table.html')

@app.route('/admin/notifications')
def notifications_settings():

  return render_template('admin-notifications.html')

@app.route('/admin/analytics')
def analytics():
  return render_template('admin-analytics.html')



## FUNCTIONS / ACTIONS ##
@app.route('/_wait_time')
def wait_time():
  rando = random.randrange(5, 50)
  wait_time = str(rando) + " minutes."
  return jsonify(result = wait_time)

@app.route('/_add_table')
def add_table():
    app.logger.debug("Got a JSON request: CREATE TABLE")
    table_id = request.args.get('table_id', "111", type=str)
    max_occupancy = request.args.get('max_occupancy', "222", type=str)
    uniqueId = uuid.uuid4()
    record = {  "type": "tables",
            "table_id": table_id,
            "max_occupancy": max_occupancy
        }
    tableCollection.insert(record)
    return jsonify(result = "true")

def get_signins():
    """
    Returns all memos in the database, in a form that
    can be inserted directly in the 'session' object.
    """
    records = [ ]
    for record in signinCollection.find( { "type": "signins" } ):
        ## Don't forgett -- arrow objects!
        del record['_id']
        records.append(record)
    return records


def get_tables():
    """
    Returns all memos in the database, in a form that
    can be inserted directly in the 'session' object.
    """
    records = [ ]
    for record in tableCollection.find( { "type": "tables" } ):
        del record['_id']
        records.append(record)
    return records

def get_notifications():
    """
    Returns all memos in the database, in a form that
    can be inserted directly in the 'session' object.
    """
    records = [ ]
    for record in notificationCollection.find( { "type": "notifications" } ):
        del record['_id']
        records.append(record)
    return records


if __name__ == "__main__":
    app.secret_key = 'super secret key'
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