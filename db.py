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
        # Accessing db
        db = client[db_name]

        # Accessing collection
        collection = db[collection_name]
        df = pandas.read_csv(csv_file_name)
        df_json = df.to_dict('records') 
        collection.insert_many(df_json)

    def import_dataframe(self, client, db_name, collection_name):
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

        # print(json_data)
        df = pandas.read_json(json_data)
        # print(df)
        return df

    def import_db(self):
        print(self.import_dataframe(self.client, self.db_name, self.collection_name))

    def export_db(self):
        print(self.export_dataframe(self.client, self.db_name, self.collection_name, self.csv_file_name))


if __name__ == '__main__':
    db_address = 'mongodb://mongodb:mongodb@172.22.0.2:27017/'
    db_name = 'demo_db'
    csv_file_name = 'shows.csv'
    collection_name = 'demo_data'
    obj = DB(db_address, db_name, collection_name, csv_file_name)
    # obj.export_db()
    obj.import_db()