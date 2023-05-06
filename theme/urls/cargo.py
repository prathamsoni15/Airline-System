from django.urls import path
from ..views.cargo import *
cargoURL=[
    path('viewCargo/',viewCargo,name="viewCargo"),
    path('addCargo/',addCargo,name="addCargo"),  
    path('updateCargo/<Airline_id>',updateCargo,name="updateCargo"), 
    path('deleteCargo/<Airline_id>',deleteCargo,name="deleteCargo"), 
    path('download_cargocsv',download_cargocsv,name="download_cargocsv"),
]