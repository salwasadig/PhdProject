import os
import pickle
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC, LinearSVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier


ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
##data = os.path.join(ROOT_DIR, '../../models/data/data.csv')
data = os.path.join(ROOT_DIR, 'data/dataset.csv')

class MLmodel():
    
    def __init__(self, path=data, X_train=None, X_test=None, Y_train=None, Y_text=None):
        self.path = path
        self.X_train = X_train
        self.X_test = X_test
        self.Y_train = Y_train
        self.Y_test = Y_text


    def get_data(self):
        df = pd.read_csv(self.path, parse_dates=['deadline','launched'])
        newdf = df.copy()
        
        newdf['country'] = newdf['country'].astype('category').cat.codes
        newdf['category'] = newdf['category'].astype('category').cat.codes
        newdf['main_category'] = newdf['main_category'].astype('category').cat.codes
        newdf['currency'] = newdf['currency'].astype('category').cat.codes
        
        to_drop = ['ID', 'name','currency','category','usd pledged','deadline','pledged','launched','goal','usd_pledged_real']

        newdf.drop(columns=to_drop, axis=1, inplace=True)

        y = newdf['state']
        
        newdf = newdf.drop('state', 1)
        self.X_train, self.X_test, self.Y_train, self.Y_test = train_test_split(newdf, y, test_size = 0.1, random_state=42)
        return self.X_train, self.X_test, self.Y_train, self.Y_test, df
        
    # Decision Tree
    def DecisionTree(self):
        decision_tree = DecisionTreeClassifier()
        decision_tree.fit(self.X_train, self.Y_train)

        # save the model to disk
        filename = 'finalized_DT_model.sav'
        pickle.dump(decision_tree, open(filename, 'wb'))


    # Random Forest
    def RandomForest(self):
        random_forest = RandomForestClassifier(n_estimators=100)
        random_forest.fit(self.X_train, self.Y_train)

        # save the model to disk
        filename = 'finalized_RF_model.sav'
        pickle.dump(random_forest, open(filename, 'wb'))
