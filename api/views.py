from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from ml_app.services import GetPredictions


class GetPredictionView(APIView):
    """
    Get price predictions from ML model
    """

    def post(self, request, format=None):
        resp = GetPredictions(request).predict()

        if resp.get('errors') is not None:
            status_code = status.HTTP_400_BAD_REQUEST
        else:
            status_code = status.HTTP_200_OK
        
        return Response(resp, status_code)
