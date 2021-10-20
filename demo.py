import pydotplus
from sklearn import tree
import matplotlib.pyplot as plt
import matplotlib.image as pltimg
from sklearn.tree import DecisionTreeClassifier
from db import DB as Database

# Uncomment print statements to observe data evolution
class SmartDecisionTreeClassifier(object):
    
    def __init__(self, dataframe):
        self.df = dataframe

    def data_mapping(self):
        for column in df:   # Iterates through all collumns in dataframe
            if (column != '_id') and (df[column].dtypes == object): # Only allows colums holding strings expect '_id' column
                yo = {} # initialize temporary json object
                # print("NAME#", column)
                df_column = df[column].drop_duplicates()    # Drops duplicates
                df_np = df_column.to_numpy()    # df_column to array
                for i in range(len(df_np)): # iterates through array elements
                    yo[df_np[i]] = i    # saving index against array element key in json object 
                self.df[column] = df[column].map(yo) # maps json object values to respective keys in dataframe
                # print(yo)
                # print()
                # print(df)
                # print()

    def extract_column_features(self):
        df_np = self.df.columns.to_numpy()
        self.features = df_np[1:-1]
        print(self.features)

    def prepare_data(self):
        self.X = self.df[self.features]
        self.Y = self.df[self.df.columns[-1]]
        # print('\nX-axes\n', self.X, '\nY-axes\n', self.Y)

    def apply_decision_tree(self):
        dtree = DecisionTreeClassifier()
        dtree = dtree.fit(self.X, self.Y)
        self.dtree_data = tree.export_graphviz(dtree, out_file=None, feature_names=self.features)
        # print(self.dtree_data)
        
    def plot_graph(self):
        self.graph = pydotplus.graph_from_dot_data(self.dtree_data)
        self.graph.write_png('mydecisiontree.png')

    def disply_graph(self):
        img=pltimg.imread('mydecisiontree.png')
        imgplot = plt.imshow(img)
        plt.show()

    def process_df(self):
        self.data_mapping()
        self.extract_column_features()
        self.prepare_data()
        self.apply_decision_tree()
        self.plot_graph()
        self.disply_graph()



if __name__ == '__main__':
    db_address = 'mongodb://mongodb:mongodb@172.22.0.2:27017/'
    db_name = 'demo_db'
    csv_file_name = 'shows.csv'
    collection_name = 'demo_data'
    db_obj = Database(db_address, db_name, collection_name, csv_file_name)
    db_obj.clear_db()
    db_obj.export_db()
    df = db_obj.import_db()
    # print(df)
    dt_obj = SmartDecisionTreeClassifier(df)
    dt_obj.process_df()