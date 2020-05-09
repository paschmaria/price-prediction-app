import logging
from datetime import timedelta

import pandas as pd
from django.conf import settings
from django.utils import timezone

from ml_app.models import Car

from .pipelines import Pipeline


def update_model():
    cars = Car.objects.all()
    df = pd.DataFrame(list(cars.values('brand', 'model', 'location', 'year', 'km_driven', 'fuel_type',
                    'transmission', 'owner_type', 'mileage', 'engine', 'power', 'seats', 'price')))
    pipeline = Pipeline(dataframe=df)
    score = pipeline.run()

    if score < settings.BASELINE_R2_SCORE:
        logging.warning("Model r2 score is below baseline")
