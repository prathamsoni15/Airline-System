from django.urls import path
from ..views.concession import *
concessionURL=[
    path('viewconcession/',viewconcession,name="viewconcession"),
    path('addconcession/',addconcession,name="addconcession"),  
    path('updateconcession/<id>',updateconcession,name="updateconcession"), 
    path('deleteconcession/<id>',deleteconcession,name="deleteconcession"), 
    path('download_concessioncsv',download_concessioncsv,name="download_concessioncsv"),
]