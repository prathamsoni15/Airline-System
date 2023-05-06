from django.urls import path
from ..views.fare import *
fareURL=[
    path('viewFare/',viewFare,name="viewFare"),
    path('addFare/',addFare,name="addFare"),  
    path('updateFare/<id>',updateFare,name="updateFare"), 
    path('deleteFare/<id>',deleteFare,name="deleteFare"), 
    path('download_farecsv',download_farecsv,name="download_farecsv"),
    
    
]