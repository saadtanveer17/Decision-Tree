import json
import pandas 
import pymongo
from bson.json_util import loads, dumps

class DB(object):

    def __init__(self, db_address, db_name, collection_name, csv_file_name):
        self.db_address = db_address
        self.db_name = db_name
        self.csv_file_name = csv_file_name
        self.collection_name = collection_name
        self.client = self.connect_to_db(self.db_address)

    def connect_to_db(self, db_address):
        # Connecting to Database server
        return pymongo.MongoClient(db_address)
        print('Yo!!!')

    def export_dataframe(self ,client, db_name, collection_name, csv_file_name):
        
        db = client[db_name]    # Accessing db
        collection = db[collection_name]    # Accessing collection
        df = pandas.read_csv(csv_file_name)
        df_json = df.to_dict('records') 
        collection.insert_many(df_json)

    def import_dataframe(self, client, db_name, collection_name):
        db = client[db_name]
        collection = db[collection_name]
        cursor = collection.find() # Now creating a Cursor instance using find() function
        list_cur = list(cursor) # Converting cursor to the list of dictionaries
        json_data = dumps(list_cur, indent = 2) # Converting to the JSON
        # print(json_data)
        self.df = pandas.read_json(json_data)
        # print(df)
        return self.df

    def clear_collection(self):
        db = self.client[self.db_name]
        collection = db[self.collection_name]
        collection.remove({})

    def import_db(self):
        return self.import_dataframe(self.client, self.db_name, self.collection_name)

    def export_db(self):
        return self.export_dataframe(self.client, self.db_name, self.collection_name, self.csv_file_name)

    def clear_db(self):
        return self.clear_collection()