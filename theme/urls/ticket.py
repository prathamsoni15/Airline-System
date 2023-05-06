from django.urls import path
from ..views.ticket import *
ticketURL=[
    path('viewTicket/',viewTicket,name="viewTicket"),
    path('addTicket/',addTicket,name="addTicket"),  
    path('updateTicket/<ticket_id>',updateTicket,name="updateTicket"), 
    path('deleteTicket/<ticket_id>',deleteTicket,name="deleteTicket"), 
    path('download_ticketcsv',download_ticketcsv,name="download_ticketcsv"),
]