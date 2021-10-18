import json
import pymongo
import pandas as pd
from bson.json_util import loads, dumps


def connect_to_db(db_address):
    # Connecting to Database server
    return pymongo.MongoClient(db_address)

def import_dataframe(client, db_name, collection_name):
    # Accessing db
    db = client[db_name]

    # Accessing collection
    collection = db[collection_name]

    # Now creating a Cursor instance using find() function
    cursor = collection.find()

    # Converting cursor to the list of dictionaries
    list_cur = list(cursor)

    # Converting to the JSON
    json_data = dumps(list_cur, indent = 2) 

    print(json_data)
    df = pd.read_json(json_data)
    print(df)
    return df


db_address = 'mongodb://mongodb:mongodb@172.22.0.3:27017/'
db_name = 'demo_db'
collection_name = 'demo_data'
client = connect_to_db(db_address)
import_dataframe(client, db_name, collection_name)