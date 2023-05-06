from socket import fromshare
from django import forms
from ..models import StatusModel
from django.db import models

class StatusForm(forms.ModelForm):
    
    class Meta:
        model=StatusModel

        fields=[
            "Flightno",
            "DepartureDate",
            "Origin",
            "Destination",
        ]