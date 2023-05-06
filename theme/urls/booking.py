from django.urls import path
from ..views.booking import *
bookingURL=[
    path('viewBooking/',viewBooking,name="viewBooking"),
    path('addBooking/',addBooking,name="addBooking"),  
    path('updateBooking/<id>',updateBooking,name="updateBooking"), 
    path('deleteBooking/<id>',deleteBooking,name="deleteBooking"), 
    path('download_bookingcsv',download_bookingcsv,name="download_bookingcsv"),
]