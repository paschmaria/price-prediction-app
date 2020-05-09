from django.urls import path

from . import views

urlpatterns = [
    path(
        "api/v1/get-predictions/",
        views.GetPredictionView.as_view(),
        name="get_predictions"
    ),
    path(
        "api/v1/create-record/",
        views.CreateUsedCarView.as_view(),
        name="create_record"
    ),
]
