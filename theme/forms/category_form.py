from socket import fromshare
from django import forms
from ..models import CategoryModel
from django.db import models

class CategoryForm(forms.ModelForm):
    
    class Meta:
        model=CategoryModel

        fields=[
            "title",
            "description",
        ]