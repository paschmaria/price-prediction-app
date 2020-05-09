import logging
from datetime import date, timedelta

import joblib
import numpy as np
import pandas as pd
from sklearn import metrics
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error as MSE
from sklearn.model_selection import train_test_split

from ml_app.mixins import GetModelMixin


class Pipeline:
    """
    Pipeline for updating prediction model using latest data
    """

    def __init__(self, dataframe):
        self.df = dataframe
        self.lr = LinearRegression()

    def preprocess(self):
        X = self.df.drop('price', axis=1)
        # get dummy variables
        X = pd.get_dummies(data=X,
                    columns=['location', 'fuel_type', 'transmission',
                        'owner_type', 'seats', 'brand', 'model'])
        # log transformation
        y = np.log1p(self.df['price'])
        split_data = train_test_split(
            X, y, test_size=0.3, random_state=101)
        return split_data

    def train(self, X, y):
        self.lr.fit(X, y)

    def test(self, X, y):
        prediction = self.lr.predict(X)
        r2score = metrics.r2_score(y, prediction)
        return r2score

    def run(self):
        X_train, X_test, y_train, y_test = self.preprocess()
        self.train(X_train, y_train)
        r2score = self.test(X_test, y_test)
        today = date.today()
        day = today.day
        month = today.month
        year = today.year
        joblib.dump(self.lr, f'../models/{year}_{month}_{day}.pkl')
        return r2score
