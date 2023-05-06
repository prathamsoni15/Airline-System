from django.shortcuts import get_object_or_404,render,redirect
from ..models import PassengerModel
from django.shortcuts import render
#from ..models import Category as CategoryForm
from ..forms.passenger_form import PassengerForm
#from ..models import Category
from django.http import HttpResponse
import csv

def viewPassenger(request):
    context={}
    context["passengers"]=PassengerModel.objects.all()
    return render(request, "passenger/view.html",context)

def addPassenger(request):
    context={}
    form=PassengerForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect( "viewPassenger")
    context['form']=form
    return render(request,"passenger/add.html",context)

def updatePassenger(request,Reg_id):
    context={}
    obj=get_object_or_404(PassengerModel,Reg_id=Reg_id)
    form=PassengerForm(request.POST or None,instance=obj)
    if form.is_valid():
        form.save()
        return redirect("viewPassenger")
    context["form"]=form
    return render(request,"passenger/edit.html",context)

def deletePassenger(request,Reg_id):
    context={}
    obj=get_object_or_404(PassengerModel,Reg_id=Reg_id)
    if request.method=="GET":
        obj.delete()
        return redirect("viewPassenger")
    return render(request,"passenger/view.html",context)


def download_passengercsv(request):
    response =HttpResponse('')
    response['Content-Disposition'] = 'attachment; filename=Passengerdetails.csv'
    writer = csv.writer(response)
    writer.writerow(['Reg_id','passport_no','f_name','l_name','email','address','contact'])
    for data in PassengerModel.objects.all():
        writer.writerow([data.Reg_id,data.passport_no,data.f_name,data.l_name,data.email,data.address,data.contact]) 

    return response