from django.shortcuts import get_object_or_404,render,redirect
from ..models import StatusModel
from django.shortcuts import render
#from ..models import Category as CategoryForm
from ..forms.status_form import StatusForm
#from ..models import Category
from django.http import HttpResponse
import csv

def viewStatus(request):
    context={}
    context["statuses"]=StatusModel.objects.all()
    return render(request, "flight_status/view.html",context)

def addStatus(request):
    context={}
    form=StatusForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect( "viewStatus")
    context['form']=form
    return render(request,"flight_status/add.html",context)

def updateStatus(request,id):
    context={}
    obj=get_object_or_404(StatusModel,id=id)
    form=StatusForm(request.POST or None,instance=obj)
    if form.is_valid():
        form.save()
        return redirect("viewStatus")
    context["form"]=form
    return render(request,"flight_status/edit.html",context)

def deleteStatus(request,id):
    context={}
    obj=get_object_or_404(StatusModel,id=id)
    if request.method=="GET":
        obj.delete()
        return redirect("viewStatus")
    return render(request,"flight_status/view.html",context)

def download_statuscsv(request):
    response =HttpResponse('')
    response['Content-Disposition'] = 'attachment; filename=Statusdetails.csv'
    writer = csv.writer(response)
    writer.writerow(['Flightno','DepartureDate','Origin','Destination'])
    for data in StatusModel.objects.all():
        writer.writerow([data.Flightno,data.DepartureDate,data.Origin,data.Destination]) 

    return response