from django.urls import path
from ..views.signup import *
SIGNUPURL=[
 
 path('signup/',signup,name="signup"),
 path('loginHandle/',loginHandle,name='loginHandle'),
 path('sup/',sup,name='sup'),
 path('logout1/',logout1,name='logout1'),
]