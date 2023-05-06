from socket import fromshare
from django import forms
from ..models import BranchModel
from django.db import models

class BranchForm(forms.ModelForm):
    
    class Meta:
        model=BranchModel

        fields=[
            "Branch_code",
            "Add1",
            "Add2",
            "City",
            "Telephone",
        ]