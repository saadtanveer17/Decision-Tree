import pandas
import numpy as np
from sklearn import tree
import pydotplus
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt
import matplotlib.image as pltimg

# importing csv data file
csv_data_frame = pandas.read_csv("heart_disease_classification_dataset.csv")
# print(csv_data_frame)
csv_data_frame = csv_data_frame.replace([np.inf, -np.inf], np.nan)
csv_data_frame = csv_data_frame.dropna()
# csv_data_frame = csv_data_frame.dropna(axis=None) 
d = {'female': 0, 'male': 1}
csv_data_frame['sex'] = csv_data_frame['sex'].map(d)
d = {'YES': 1, 'NO': 0}
csv_data_frame['target'] = csv_data_frame['target'].map(d)

features = ['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg', 'thalach', 'exang', 'oldpeak', 'slope', 'ca', 'thal']

X = csv_data_frame[features]
y = csv_data_frame['target']


# # iterating over rows using iterrows() function
# for i, j in csv_data_frame.iterrows():
#     print(i, j)
#     print()

# for column in csv_data_frame:
#     print("NAME#", column)
#     print(len(csv_data_frame[column].unique()))
#     print()

# d = {'UK': 0, 'USA': 1, 'N': 2}
# csv_data_frame['Nationality'] = csv_data_frame['Nationality'].map(d)
# d = {'YES': 1, 'NO': 0}
# csv_data_frame['Go'] = csv_data_frame['Go'].map(d)

# features = ['Age', 'Experience', 'Rank', 'Nationality']

# X = csv_data_frame[features]
# y = csv_data_frame['Go']
print(X)
dtree = DecisionTreeClassifier()
dtree = dtree.fit(X, y)
# data = tree.export_graphviz(dtree, out_file=None, feature_names=features)
# graph = pydotplus.graph_from_dot_data(data)
# print(graph)
# graph.write_png('mydecisiontree.png')

# img=pltimg.imread('mydecisiontree.png')
# imgplot = plt.imshow(img)
# plt.show()