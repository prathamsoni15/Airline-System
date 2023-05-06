from django.shortcuts import get_object_or_404,render,redirect
from ..models import CargoModel
from django.shortcuts import render
#from ..models import Category as CategoryForm
from ..forms.cargo_form import CargoForm
#from ..models import Category
from django.http import HttpResponse
import csv

def viewCargo(request):
    context={}
    context["cargoes"]=CargoModel.objects.all()
    return render(request, "cargo/view.html",context)

def addCargo(request):
    context={}
    form=CargoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect( "viewCargo")
    context['form']=form
    return render(request,"cargo/add.html",context)

def updateCargo(request,Airline_id):
    context={}
    obj=get_object_or_404(CargoModel,Airline_id=Airline_id)
    form=CargoForm(request.POST or None,instance=obj)
    if form.is_valid():
        form.save()
        return redirect("viewCargo")
    context["form"]=form
    return render(request,"cargo/edit.html",context)

def deleteCargo(request,Airline_id):
    context={}
    obj=get_object_or_404(CargoModel,Airline_id=Airline_id)
    if request.method=="GET":
        obj.delete()
        return redirect("viewCargo")
    return render(request,"cargo/view.html",context)

def download_cargocsv(request):
    response =HttpResponse('')
    response['Content-Disposition'] = 'attachment; filename=Cargodetails.csv'
    writer = csv.writer(response)
    writer.writerow(['Airline_id','Origin','Destination','Date','Goods_Description','Weight','Product'])
    for data in CargoModel.objects.all():
        writer.writerow([data.Airline_id,data.Origin,data.Destination,data.Date,data.Goods_Description,data.Weight,data.Product]) 

    return response