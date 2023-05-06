from socket import fromshare
from django import forms
from ..models import FeedbackModel
from django.db import models

class FeedbackForm(forms.ModelForm):
    
    class Meta:
        model=FeedbackModel

        fields=[
            "Quality_Score",
            "Message",
        ]