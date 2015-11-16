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
           "name": "John",
           "check_time": arrow.utcnow().naive,
           "seat_time": "False",
           "leave_time": "False",
           "party_size": 5,
           "table_id": "identifier",
           "requests": "This is a sample memo",
           "contacted": "true"
          }

signinCollection.insert(record)


record = { "type": "signins",
           "name": "Jeff",
           "check_time": arrow.utcnow().replace(days=+1).naive,
           "seat_time": "False",
           "leave_time": "False",
           "party_size": 12,
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

##### NOTIFICATIONS #####

record = {  "type": "notifications",
            "id": "demo",
            "text_time": 5,
            "text_message": "Stringity string strang you"
        }

notificationCollection.insert(record)

##### RESTAURANT INFO #####

record = { "type": "restaurant_info",
           "id": "demo",
           "name": "Glenwood",
           "op_hours": "9AM to 5PM"
        }

restaurantCollection.insert(record)

#
# Read database --- May be useful to see what is in there,
# even after you have a working 'insert' operation in the flask app,
# but they aren't very readable.  If you have more than a couple records,
# you'll want a loop for printing them in a nicer format. 
#

signinRecords = [ ] 
tableRecords = [ ]
for record in signinCollection.find( { "type": "signins" } ):
  signinRecords.append(
    {  "type": record['type'],
       "name": record['name'],
       "check_time": arrow.get(record['check_time']).to('local').isoformat(),
       "seat_time": record['seat_time'],
       "leave_time": record['leave_time'],
       "party_size": record['party_size'],
       "table_id": record['table_id'],
       "requests": record['requests'],
       "contacted": record['contacted']
      })

for record in tableCollection.find( { "type": "tables"} ):
  tableRecords.append({  
    "type": record['type'],
    "table_id": record['table_id'],
    "max_occupancy": record['max_occupancy']
  })


print(signinRecords)
print(tableRecords)
