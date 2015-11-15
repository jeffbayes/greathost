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

except:
    print("Failure opening database.  Is Mongo running? Correct password?")
    sys.exit(1)

#
# Insertions:  I commented these out after the first
# run successfuly inserted them
# 

##### SIGN INS #####

record = { "type": "signins",
           "name": "John",
           "check_time": arrow.utcnow().naive,
           "seat_time": arrow.utcnow().naive,
           "leave_time": arrow.utcnow().naive,
           "party_size": 5,
           "table_id": "identifier",
           "requests": "This is a sample memo",
           "contacted": "true"
          }

signinCollection.insert(record)


record = { "type": "signins",
           "name": "Jeff",
           "check_time": arrow.utcnow().replace(days=+1).naive,
           "seat_time": arrow.utcnow().replace(days=+1).naive,
           "leave_time": arrow.utcnow().replace(days=+1).naive,
           "party_size": 12,
           "table_id": "iagasegsrgr",
           "requests": "This is a samplae megagmo",
           "contacted": "true"
          }

signinCollection.insert(record)

##### TABLES #####


#
# Read database --- May be useful to see what is in there,
# even after you have a working 'insert' operation in the flask app,
# but they aren't very readable.  If you have more than a couple records,
# you'll want a loop for printing them in a nicer format. 
#

records = [ ] 
for record in signinCollection.find( { "type": "signins" } ):
  records.append(
    {  "type": record['type'],
       "name": record['name'],
       "check_time": arrow.get(record['check_time']).to('local').isoformat(),
       "seat_time": arrow.get(record['seat_time']).to('local').isoformat(),
       "leave_time": arrow.get(record['leave_time']).to('local').isoformat(),
       "party_size": record['party_size'],
       "requests": record['requests'],
       "contacted": record['contacted']
      })

print(records)
