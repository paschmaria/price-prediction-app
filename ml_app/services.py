import logging

import numpy as np
import pandas as pd
import joblib

from .constants import ONE_HOT_ENCODED_COLUMNS
from .exceptions import PreprocessingException
from .forms import UsedCarForm
from .utils import process_name


lr = joblib.load('./model.pkl')

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
            
            try:
                data = self.preprocess(data)
            except PreprocessingException:
                return {
                    'errors': [{
                        'request': 'there was a problem with your request'
                    }]
                }

            return { 'data': data, }
        else:
            return { 'errors': form.errors, }

    def preprocess(self, data):
        columns = ONE_HOT_ENCODED_COLUMNS
        data_dict = {k: 0 for k in columns}
        brand, model, _ = process_name(data.pop('name'))
        location = data.pop('location')
        fuel_type = data.pop('fuel_type')
        transmission = data.pop('transmission')
        owner_type = data.pop('owner_type')

        try:
            # handle categorical variables
            data_dict[f'Brand_{brand.lower()}'] = 1
            data_dict[f'Model_{model.lower()}'] = 1
            data_dict[f'Location_{location}'] = 1
            data_dict[f'Fuel_Type_{fuel_type}'] = 1
            data_dict[f'Transmission_{transmission}'] = 1
            data_dict[f'Owner_Type_{owner_type}'] = 1
        except (KeyError, Exception) as e:
            logging.error(e)
            raise PreprocessingException

        # handle other variables
        data_dict['Kilometers_Driven'] = data.pop('km_driven')
        for key in data.keys():
            data_dict[key.capitalize()] = data[key]

        return data_dict

    def predict(self):
        resp = self.validate(self.data)

        if resp.get('errors') is not None:
            return resp
        
        # get preprocessed data
        data = resp.get('data')
        # convert to dataframe
        X = pd.DataFrame(**data)
        # get predictions
        y_pred_log = lr.predict(X)
        # get inverse of log transformation
        y_pred = np.expm1(y_pred_log)
        return { 'prediction': y_pred }
        