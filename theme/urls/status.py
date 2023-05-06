from django.urls import path
from ..views.status import *
statusURL=[
    path('viewStatus/',viewStatus,name="viewStatus"),
    path('addStatus/',addStatus,name="addStatus"),  
    path('updateStatus/<id>',updateStatus,name="updateStatus"), 
    path('deleteStatus/<id>',deleteStatus,name="deleteStatus"),
    path('download_statuscsv',download_statuscsv,name="download_statuscsv"), 
]