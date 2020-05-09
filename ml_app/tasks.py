from __future__ import absolute_import, unicode_literals

from celery import task

from .jobs.update_model import update_model

@task
def update_ml_model():
    update_model()