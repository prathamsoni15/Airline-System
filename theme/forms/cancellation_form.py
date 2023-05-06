from socket import fromshare
from django import forms
from ..models import CancellationModel
from django.db import models

class CancellationForm(forms.ModelForm):
    
    class Meta:
        model=CancellationModel

        fields=[
            "Cancel_id",
            "Booking_id",
            "Cancel_Date",
            "Refund_Money",
        ]