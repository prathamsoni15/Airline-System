from django import forms  
#from django.contrib.auth.models import UserCreationForm
#from django.db import forms
from ..models import SignUp
 
class SignUpForm(forms.ModelForm):  
    class Meta:  
        model = SignUp  
        fields = ('username','email','phone','password',)