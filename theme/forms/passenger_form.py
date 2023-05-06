from socket import fromshare
from django import forms
from ..models import PassengerModel
from django.db import models

class PassengerForm(forms.ModelForm):
    
    class Meta:
        model=PassengerModel

        fields=[
            "Reg_id",
            "passport_no",
            "f_name",
            "l_name",
            "email",
            "address",
            "contact",
        ]