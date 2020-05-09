from datetime import timedelta

from django.utils import timezone

from ml_app.models import Car

from .pipelines import Pipeline


def update_model():
    yesterday = timezone.now() - timedelta(days=1)
    last_record = Car.objects.filter(created__gte=yesterday)

    if last_record.exists():
        pass