from socket import fromshare
from django import forms
from ..models import AirlineModel
from django.db import models

class AirlineForm(forms.ModelForm):
    
    class Meta:
        model=AirlineModel

        fields=[
            "Airline_id",
            "From",
            "To",
            "Departing_Date",
            "Returning_Date",
            "Class",
        ]