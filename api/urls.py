from django.urls import path
from rest_framework.authtoken import views as auth_views

from . import views


urlpatterns = [
    path("api/auth/", auth_views.obtain_auth_token),
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
