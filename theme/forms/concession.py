from socket import fromshare
from django import forms
from ..models import concessionModel
from django.db import models

class concessionForm(forms.ModelForm):
    
    class Meta:
        model=concessionModel

        fields=[
            "Booking_id",
            "Flightno",
            "Extra_Baggage_Allowance",
            "Fare",
        ]