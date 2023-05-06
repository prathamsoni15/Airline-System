from django.urls import path
from ..views.passenger import *
passengerURL=[
    path('viewPassenger/',viewPassenger,name="viewPassenger"),
    path('addPassenger/',addPassenger,name="addPassenger"),  
    path('updatePassenger/<Reg_id>',updatePassenger,name="updatePassenger"), 
    path('deletePassenger/<Reg_id>',deletePassenger,name="deletePassenger"), 
    path('download_passengercsv',download_passengercsv,name="download_passengercsv"),
]