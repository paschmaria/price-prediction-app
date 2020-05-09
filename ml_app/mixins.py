import joblib

from .exceptions import PredictionException


class GetModelMixin:
    """
    Mixin for getting latest model version using date
    """

    def get_model(self, date):
        year = date.year
        month = date.month
        day = date.day

        try:
            model = joblib.load(f'./models/{year}_{month}_{day}.pkl')
        except FileNotFoundError:
            raise PredictionException
        
        return model