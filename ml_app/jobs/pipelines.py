import logging
from datetime import date, timedelta

import numpy as np
from sklearn import metrics
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error as MSE
from sklearn.model_selection import train_test_split

from ml_app.mixins import GetModelMixin


class Pipeline(GetModelMixin):
    """
    Pipeline for updating prediction model using latest data
    """

    def __init__(self, dataframe):
        self.df = dataframe
        self.lr = LinearRegression()

    def preprocess(self):
        X = self.df.drop('price', axis=1)
        # log transformation
        y = np.log1p(self.df['price'])
        split_data = train_test_split(
            X, y, test_size=0.3, random_state=101)
        return split_data

    def train(self, X, y):
        return self

    def test(self, X, y):
        yesterday = date.today() - timedelta(days=1)
        model = self.get_model(yesterday)
        prediction = model.predict(X)
        r2score = metrics.r2_score(y, prediction)
        return r2score

    def run(self, train=True):
        X_train, X_test, y_train, y_test = self.preprocess()

        if train:
            self.train(X_train, y_train)
        
        r2score = self.test(X_test, y_test)
        return r2score

# pipeline receives preprocessed data
# trains model using data if train = True
# runs predictions and returns R2