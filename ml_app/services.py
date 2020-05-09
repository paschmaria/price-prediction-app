from datetime import datetime
import logging

import numpy as np
import pandas as pd
import joblib

from .constants import ONE_HOT_ENCODED_COLUMNS
from .exceptions import PreprocessingException, PredictionException
from .forms import UsedCarForm
from .utils import process_name


class GetPredictions:
    """
    Process data from request object and return prediction
    """

    def __init__(self, request):
        self.data = request.data

    def validate(self, data):
        form = UsedCarForm(data)

        if form.is_valid():
            data = form.cleaned_data
            date, data = self.preprocess(data)
            
            return {
                'date': date,
                'data': data,
            }
        else:
            return { 'errors': form.errors, }

    def preprocess(self, data):
        columns = ONE_HOT_ENCODED_COLUMNS
        data_dict = {k: [0] for k in columns}
        date = data.pop('price_date')
        brand, model, _ = process_name(data.pop('name'))
        location = data.pop('location')
        fuel_type = data.pop('fuel_type')
        transmission = data.pop('transmission')
        owner_type = data.pop('owner_type')
        seats = data.pop('seats')

        # handle categorical variables
        data_dict[f'Brand_{brand.lower()}'] = [1]
        data_dict[f'Model_{model.lower()}'] = [1]
        data_dict[f'Location_{location}'] = [1]
        data_dict[f'Fuel_Type_{fuel_type}'] = [1]
        data_dict[f'Transmission_{transmission}'] = [1]
        data_dict[f'Owner_Type_{owner_type}'] = [1]
        data_dict[f'Seats_{seats}'] = [1]

        # handle other variables
        data_dict['Kilometers_Driven'] = [data.pop('km_driven')]
        for key in data.keys():
            data_dict[key.capitalize()] = [data[key]]

        return date, data_dict

    def get_model(self, date):
        year = date.year
        month = date.month
        day = date.day

        try:
            model = joblib.load(f'./models/{year}_{month}_{day}.pkl')
        except FileNotFoundError:
            raise PredictionException
        
        return model

    def predict(self):
        resp = self.validate(self.data)

        if resp.get('errors') is not None:
            return resp
            
        # get desired price date
        date = resp.get('date')
        date = datetime.strptime(date)
        
        try:
            lr = self.get_model(date)
        except PredictionException:
            return { 'errors': f'no price prediction was gotten \
                                    for {date.strftime("%Y/%d/%m")}' }
        
        # get preprocessed data
        data = resp.get('data')
        # convert to dataframe
        X = pd.DataFrame.from_dict(data)
        # get predictions
        y_pred_log = lr.predict(X)
        # get inverse of log transformation
        y_pred = np.expm1(y_pred_log)
        return { 'prediction': y_pred.round(2) }
        