from __future__ import absolute_import

import os

from celery import Celery
from celery.schedules import crontab
from django.conf import settings
from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv(filename='env/prod.env'))
# set the default Django settings module for the 'celery' program.
app = Celery('core')

# Using a string here means the worker will not have to
# pickle the object when using Windows.
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

app.conf.beat_schedule = {
    'run-every-morning': {
        'task': 'tasks.update_ml_model',
        'schedule': crontab(hour=1),
        'args': (),
    },
}