from socket import fromshare
from django import forms
from ..models import FareModel
from django.db import models

class FareForm(forms.ModelForm):
    
    class Meta:
        model=FareModel

        fields=[
            "Route_No",
            "AIR_Bus_No",
            "First_Fare",
            "Business_Fare",
            "Economy_Fare",
        ]