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
data = os.path.join(ROOT_DIR, 'data/data.csv')

class MLmodel():
    
    def __init__(self, path=data, X_train=None, X_test=None, Y_train=None, Y_text=None):
        self.path = path
        self.X_train = X_train
        self.X_test = X_test
        self.Y_train = Y_train
        self.Y_test = Y_text

    def get_data(self):
        df = pd.read_csv(self.path)
        df.dropna(how='any', axis=0, inplace=True)
    
        
        df['category'] = df['category'].astype('category').cat.codes
        df['main_category'] = df['main_category'].astype('category').cat.codes
        df['currency'] = df['currency'].astype('category').cat.codes
        df['deadline'] = pd.to_datetime(df['deadline'], format='%d/%m/%Y').dt.date
        df['launched'] = pd.to_datetime(df['launched'], format='%d/%m/%Y %H:%M').dt.date
        df['country'] = df['country'].astype('category').cat.codes

        df['duration_days'] = df['deadline'].subtract(df['launched']).dt.days
        df['state'] = df['state'].astype('category')
        df['state'] = df['state'].map({'failed': 0,'successful': 1})

        to_drop = ['ID', 'name','currency','category','usd pledged','deadline','pledged','launched','goal','usd_pledged_real']

        new_df = df.drop(columns=to_drop, axis=1)
    
        new_df.dropna(how='any', axis=0, inplace=True)

        y = new_df['state']
        
        new_df = new_df.drop('state', 1)
        self.X_train, self.X_test, self.Y_train, self.Y_test = train_test_split(new_df, y, test_size = 0.1, random_state=42)
        return self.X_train, self.X_test, self.Y_train, self.Y_test, new_df
        
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
