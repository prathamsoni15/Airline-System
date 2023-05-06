from pyexpat.errors import messages
from django.shortcuts import get_object_or_404,render,redirect
from ..models import BookingModel
from django.shortcuts import render
#from ..models import Category as CategoryForm
from ..forms.booking_form import BookingForm
#from ..models import Category
from http.client import HTTPResponse
from django.http import HttpResponse
import csv

def viewBooking(request):
    context={}
    context["bookings"]=BookingModel.objects.all()
    return render(request, "booking/view.html",context)

def addBooking(request):
    context={}
    form=BookingForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect( "viewBooking")
    context['form']=form
    return render(request,"booking/add.html",context)

def updateBooking(request,Booking_id):
    context={}
    obj=get_object_or_404(BookingModel,Booking_id=Booking_id)
    form=BookingForm(request.POST or None,instance=obj)
    if form.is_valid():
        form.save()
        return redirect("viewBooking")
    context["form"]=form
    return render(request,"booking/edit.html",context)

def deleteBooking(request,Booking_id):
    context={}
    obj=get_object_or_404(BookingModel,Booking_id=Booking_id)
    if request.method=="GET":
        obj.delete()
        return redirect("viewBooking")
    return render(request,"booking/view.html",context)

def download_bookingcsv(request):
    response =HttpResponse('')
    response['Content-Disposition'] = 'attachment; filename=bookingdetails.csv'
    writer = csv.writer(response)
    writer.writerow(['Booking_id','Firstname','Lastname','Mobile_number'])
    for data in BookingModel.objects.all():
        writer.writerow([data.Booking_id,data.Firstname,data.Lastname,data.Mobile_number]) 

    return response
