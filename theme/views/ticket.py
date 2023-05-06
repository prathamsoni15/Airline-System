from django.shortcuts import get_object_or_404,render,redirect
from ..models import TicketModel
from django.shortcuts import render
#from ..models import Category as CategoryForm
from ..forms.ticket_form import TicketForm
#from ..models import Category
from django.http import HttpResponse
import csv

def viewTicket(request):
    context={}
    context["tickets"]=TicketModel.objects.all()
    return render(request, "ticket/view.html",context)

def addTicket(request):
    context={}
    form=TicketForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect( "viewTicket")
    context['form']=form
    return render(request,"ticket/add.html",context)

def updateTicket(request,ticket_id):
    context={}
    obj=get_object_or_404(TicketModel,ticket_id=ticket_id)
    form=TicketForm(request.POST or None,instance=obj)
    if form.is_valid():
        form.save()
        return redirect("viewTicket")
    context["form"]=form
    return render(request,"ticket/edit.html",context)

def deleteTicket(request,ticket_id):
    context={}
    obj=get_object_or_404(TicketModel,ticket_id=ticket_id)
    if request.method=="GET":
        obj.delete()
        return redirect("viewTicket")
    return render(request,"ticket/view.html",context)

def download_ticketcsv(request):
    response =HttpResponse('')
    response['Content-Disposition'] = 'attachment; filename=Ticketdetails.csv'
    writer = csv.writer(response)
    writer.writerow(['ticket_id','Booking_id','Reg_id','destination_id','depart_date','return_date'])
    for data in TicketModel.objects.all():
        writer.writerow([data.ticket_id,data.Booking_id,data.Reg_id,data.destination_id,data.depart_date,data.return_date]) 

    return response