from socket import fromshare
from django import forms
from ..models import CargoModel
from django.db import models

class CargoForm(forms.ModelForm):
    
    class Meta:
        model=CargoModel

        fields=[
            "Airline_id",
            "Origin",
            "Destination",
            "Date",
            "Goods_Description",
            "Weight",
            "Product",
        ]