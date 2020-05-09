from django import forms


class UsedCarForm(forms.Form):
    """
    Forms for validating car record
    """

    price_date = forms.DateField()
    name = forms.CharField(max_length=225)
    location = forms.CharField(max_length=100)
    year = forms.IntegerField(min_value=1885) # min value: when the first car was ever made
    km_driven = forms.IntegerField(min_value=0)
    fuel_type = forms.CharField(max_length=50)
    transmission = forms.CharField(max_length=50)
    owner_type = forms.CharField(max_length=50)
    mileage = forms.DecimalField(max_digits=10, decimal_places=2)
    engine = forms.DecimalField(max_digits=10, decimal_places=2)
    power = forms.DecimalField(max_digits=10, decimal_places=2)
    seats = forms.FloatField()
