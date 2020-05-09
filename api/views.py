from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from ml_app.services import GetPredictions

from .serializers import CarSerializer


class GetPredictionView(APIView):
    """
    Get User Car price predictions from ML model
    """
    permission_classes = (IsAuthenticated,)

    def post(self, request, format=None):
        resp = GetPredictions(request).predict()

        if resp.get('errors') is not None:
            status_code = status.HTTP_400_BAD_REQUEST
        else:
            status_code = status.HTTP_200_OK
        
        return Response(resp, status_code)


class CreateUsedCarView(CreateAPIView):
    """
    Create new records from observations in the marketplace
    """

    serializer_class = CarSerializer
    permission_classes = (IsAuthenticated,)