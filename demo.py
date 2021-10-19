import pandas
from sklearn import tree
import pydotplus
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt
import matplotlib.image as pltimg
import json
import pymongo
from bson.json_util import loads, dumps
import db

db_address = 'mongodb://mongodb:mongodb@172.22.0.3:27017/'
db_name = 'demo_db'
collection_name = 'demo_data'
client = db.connect_to_db(db_address)
# db.export_dataframe(client, db_name, collection_name, csv_file_name)
df = db.import_dataframe(client, db_name, collection_name)

print(df)
for column in df:
    if (column != '_id') and (df[column].dtypes == object):
        yo = {}
        print("NAME#", column)
        df_column = df[column].drop_duplicates()
        df_np = df_column.to_numpy()
        for i in range(len(df_np)):
            yo[df_np[i]] = i
        df[column] = df[column].map(yo)
        print(yo)
        print()
        print(df)
        print()


# d = {'UK': 0, 'USA': 1, 'N': 2}
# df['Nationality'] = df['Nationality'].map(d)
# d = {'YES': 1, 'NO': 0}
# df['Go'] = df['Go'].map(d)
# features = ['Age', 'Experience', 'Rank', 'Nationality']

df_np = df.columns.to_numpy()
features = df_np[1:-1]
print(features)

X = df[features]
y = df['Go']

print(X, y)
dtree = DecisionTreeClassifier()
dtree = dtree.fit(X, y)
data = tree.export_graphviz(dtree, out_file=None, feature_names=features)
graph = pydotplus.graph_from_dot_data(data)
graph.write_png('mydecisiontree.png')

img=pltimg.imread('mydecisiontree.png')
imgplot = plt.imshow(img)
plt.show()