from rest_framework import serializers

from ml_app.models import Car


class CarSerializer(serializers.ModelSerializer):
    """
    Serializes the car model instance to JSON format
    """

    class Meta:
        model = Car
        fields = (
           'brand',
            'model',
            'location',
            'year',
            'km_driven',
            'fuel_type',
            'transmission',
            'owner_type',
            'mileage',
            'engine',
            'power',
            'seats',
            'price', 
        )
