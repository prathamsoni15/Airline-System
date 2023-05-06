from socket import fromshare
from django import forms
from ..models import BookingModel
from django.db import models

class BookingForm(forms.ModelForm):
    
    class Meta:
        model=BookingModel

        fields=[
            "Booking_id",
            "Firstname",
            "Lastname",
            "Mobile_number",
        ]