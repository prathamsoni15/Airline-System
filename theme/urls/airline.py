from django.urls import path
from ..views.airline import *
airlineURL=[
    path('viewAirline/',viewAirline,name="viewAirline"),
    path('addAirline/',addAirline,name="addAirline"),  
    path('updateAirline/<Airline_id>',updateAirline,name="updateAirline"), 
    path('deleteAirline/<Airline_id>',deleteAirline,name="deleteAirline"), 
    path('download_airlinecsv',download_airlinecsv,name='download_airlinecsv'),
    path('bulkUpload/',bulk_upload,name='bulkUpload'),
    path('upload_csv/',upload_csv,name='upload_csv'),
    #path('download_csv/',download_csv,name='download_csv'),
]