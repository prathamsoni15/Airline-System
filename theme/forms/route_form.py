from socket import fromshare
from django import forms
from ..models import RouteModel
from django.db import models

class RouteForm(forms.ModelForm):
    
    class Meta:
        model=RouteModel

        fields=[
            "Route_No",
            "Description",
            "From",
            "To",
        ]