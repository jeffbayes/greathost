"""
Just to test database functions,
outside of Flask.

We want to open our MongoDB database,
insert some memos, and read them back
"""
import arrow

# Mongo database
from pymongo import MongoClient
import CONFIG
try: 
    dbclient = MongoClient(CONFIG.MONGO_URL)
    db = dbclient.greathost
    signinCollection = db.signins
    tableCollection = db.tables
    notificationCollection = db.notifications
    restaurantCollection = db.restaurants

except:
    print("Failure opening database. Is Mongo running? Correct password?")
    sys.exit(1)

#
# Insertions:  I commented these out after the first
# run successfuly inserted them
# 

##### SIGN INS #####

record = { "type": "signins",
           "name": "Anders",
           "check_time": "6:30",
           "seat_time": "6:45",
           "leave_time": "False",
           "party_size": 2,
           "table_id": "identifier",
           "requests": "This is a sample memo",
           "contacted": "true"
          }


signinCollection.insert(record)

record = { "type": "signins",
           "name": "Stanley",
           "check_time": "6:32",
           "seat_time": "False",
           "leave_time": "False",
           "party_size": 20,
           "table_id": "identifier",
           "requests": "This is a sample memo",
           "contacted": "true"
          }

record = { "type": "signins",
           "name": "Rebecca",
           "check_time": "6:34",
           "seat_time": "6:41",
           "leave_time": "False",
           "party_size": 2,
           "table_id": "identifier",
           "requests": "This is a sample memo",
           "contacted": "true"
          }

signinCollection.insert(record)

record = { "type": "signins",
           "name": "John",
           "check_time": "6:35",
           "seat_time": "False",
           "leave_time": "False",
           "party_size": 5,
           "table_id": "identifier",
           "requests": "This is a sample memo",
           "contacted": "true"
          }

signinCollection.insert(record)


record = { "type": "signins",
           "name": "Matthew",
           "check_time": "6:42",
           "seat_time": "False",
           "leave_time": "False",
           "party_size": 4,
           "table_id": "iagasegsrgr",
           "requests": "This is a samplae megagmo",
           "contacted": "true"
          }

signinCollection.insert(record)

##### TABLES #####



record = {  "type": "tables",
            "table_id": "22",
            "max_occupancy": "5"
}
tableCollection.insert(record)
record = {  "type": "tables",
            "table_id": "2",
            "max_occupancy": "7"
        }
tableCollection.insert(record)
record = {  "type": "tables",
            "table_id": "3",
            "max_occupancy": "2"
        }
tableCollection.insert(record)
record = {  "type": "tables",
            "table_id": "4",
            "max_occupancy": "7"
        }
tableCollection.insert(record)
record = {  "type": "tables",
            "table_id": "5",
            "max_occupancy": "2"
        }
tableCollection.insert(record)
record = {  "type": "tables",
            "table_id": "6",
            "max_occupancy": "4"
        }
tableCollection.insert(record)
record = {  "type": "tables",
            "table_id": "7",
            "max_occupancy": "4"
        }
tableCollection.insert(record)
record = {  "type": "tables",
            "table_id": "8",
            "max_occupancy": "4"
        }
record = {  "type": "tables",
            "table_id": "1",
            "max_occupancy": "5"
        }

tableCollection.insert(record)

##### NOTIFICATIONS #####

# record = {  "type": "notifications",
#             "id": "demo",
#             "text_time": 5,
#             "text_message": "Stringity string strang you"
#         }

# notificationCollection.insert(record)

# ##### RESTAURANT INFO #####

# record = { "type": "restaurant_info",
#            "id": "demo",
#            "name": "Glenwood",
#            "op_hours": "9AM to 5PM"
#         }

# restaurantCollection.insert(record)

#
# Read database --- May be useful to see what is in there,
# even after you have a working 'insert' operation in the flask app,
# but they aren't very readable.  If you have more than a couple records,
# you'll want a loop for printing them in a nicer format. 
#