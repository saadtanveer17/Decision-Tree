import json
import pymongo
import pandas as pd
from bson.json_util import loads, dumps

# Connecting to Database server
client = pymongo.MongoClient('mongodb://mongodb:mongodb@172.22.0.3:27017/')

# Accessing db
db = client.demo_db

# Accessing collection
collection = db.demo_data

# Now creating a Cursor instance using find() function
cursor = collection.find()

# Converting cursor to the list of dictionaries
list_cur = list(cursor)

# Converting to the JSON
json_data = dumps(list_cur, indent = 2) 

print(json_data)
df = pd.read_json(json_data)
print(df)