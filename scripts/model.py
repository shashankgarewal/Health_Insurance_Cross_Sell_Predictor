import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.pipeline import Pipeline
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.preprocessing import TargetEncoder

from sklearn.model_selection import train_test_split, GridSearchCV, StratifiedKFold
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier
from sklearn.metrics import classification_report, average_precision_score, roc_auc_score

init_df = pd.read_csv('../dataset/train.csv')
df = init_df.copy()

class CleanData(BaseEstimator, TransformerMixin):
    def fit(self, X, y=None):
        return self
    
    def transform(self, X):
        X = X.copy()
        if 'id' in X.columns:
            X.drop(columns=['id'], inplace=True)
        return X
    
class CategoricalTransformer(BaseEstimator, TransformerMixin):
    def fit(self, X, y=None):
        return self 
    
    def transform(self, X):
        X = X.copy()
        X['Gender']         = X['Gender'].replace({'Female': 0, 'Male': 1})
        X['Vehicle_Damage'] = X['Vehicle_Damage'].replace({'Yes': 1, 'No': 0})
        X['Vehicle_Age']    = X['Vehicle_Age'].replace({'< 1 Year': 1, '1-2 Year': 2, '> 2 Years': 3})
        return X
    
class FeatureInteractor(BaseEstimator, TransformerMixin):
    def fit(self, X, y=None):
        return self
    
    def transform(self, X):
        # feature interaction
        X["Insurance_History"] = X["Previously_Insured"] * X["Vehicle_Damage"]
        X["Age_to_VehicleAge_Ratio"] = X["Age"] / (X["Vehicle_Age"] + 1)
        X["Age_PolicyChannel"] = X["Age"] * X["Policy_Sales_Channel"]
        X["Insured_PolicyChannel"] = X["Previously_Insured"] * X["Encoded_Policy_Channel"]
        return X
    
class CardinalityTransformer(BaseEstimator, TransformerMixin):
    # k-fold target encoding with weighted mean
    def __init__(self):
        self.encoder = TargetEncoder()
        self.high_card_cols = ['Region_Code', 'Policy_Sales_Channel']
        
        
    def fit(self, X, y=None):
        self.encoder.fit(X[self.high_card_cols], y)
        return self
    
    def transform(self, X):
        X[self.high_card_cols] = self.encoder.transform(X[self.high_card_cols])
        return X
            

    
data_pipeline = Pipeline(steps=[('clean_data', CleanData()), 
                                ('cat2num', CategoricalTransformer()), 
                                ('num2mean', CardinalityTransformer())
                                ])

