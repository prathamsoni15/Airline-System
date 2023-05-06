from socket import fromshare
from django import forms
from ..models import TicketModel
from django.db import models

class TicketForm(forms.ModelForm):
    
    class Meta:
        model=TicketModel

        fields=[
            "ticket_id",
            "Booking_id",
            "Reg_id",
            "destination_id",
            "depart_date",
            "return_date", 
        ]