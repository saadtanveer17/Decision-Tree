import json
import pymongo
import pandas as pd

# Connecting MongoDB Client
client = pymongo.MongoClient('mongodb://mongodb:mongodb@172.22.0.3:27017/')
db = client.demo_db
collection = db.demo_data
df = pd.read_csv("shows.csv")
df_json = df.to_dict('records') 
collection.insert_many(df_json)

# df['json'] = df.apply(lambda x: x.to_json(), axis=1)

# df = pd.read_csv('shows.csv',encoding = 'ISO-8859-1')   # loading csv file
# df.to_json('shows.json')                               # saving to json file
# jdf = open('shows.json').read()                        # loading the json file 
# data = json.loads(jdf)
# print(data)
# db.insert_many(data)

# def csv_to_json(filename, header=None):
#     data = pd.read_csv(filename, header=header)
#     return data.to_dict('records')

# json_data = csv_to_json('shows.csv')
# print(json_data)
# db.insert_many(json_data)
