from django.urls import path
from ..views.cancel import *
cancelURL=[
    path('viewCancel/',viewCancel,name="viewCancel"),
    path('addCancel/',addCancel,name="addCancel"),  
    path('updateCancel/<Cancel_id>',updateCancel,name="updateCancel"), 
    path('deleteCancel/<Cancel_id>',deleteCancel,name="deleteCancel"), 
    path('download_cancelcsv',download_cancelcsv,name="download_cancelcsv"),
]