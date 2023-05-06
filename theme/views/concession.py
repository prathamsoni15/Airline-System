from django.shortcuts import get_object_or_404,render,redirect
from ..models import concessionModel
from django.shortcuts import render
#from ..models import Category as CategoryForm
from ..forms.concession import concessionForm
#from ..models import Category
from django.http import HttpResponse
import csv

def viewconcession(request):
    context={}
    context["concessions"]=concessionModel.objects.all()
    return render(request, "concession/view.html",context)

def addconcession(request):
    context={}
    form=concessionForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect( "viewconcession")
    context['form']=form
    return render(request,"concession/add.html",context)

def updateconcession(request,id):
    context={}
    obj=get_object_or_404(concessionModel,id=id)
    form=concessionForm(request.POST or None,instance=obj)
    if form.is_valid():
        form.save()
        return redirect("viewconcession")
    context["form"]=form
    return render(request,"concession/edit.html",context)

def deleteconcession(request,id):
    context={}
    obj=get_object_or_404(concessionModel,id=id)
    if request.method=="GET":
        obj.delete()
        return redirect("viewconcession")
    return render(request,"concession/view.html",context)

def download_concessioncsv(request):
    response =HttpResponse('')
    response['Content-Disposition'] = 'attachment; filename=Concesssiondetails.csv'
    writer = csv.writer(response)
    writer.writerow(['Booking_id','Flightno','Extra_Baggage_Allowance','Fare',])
    for data in concessionModel.objects.all():
        writer.writerow([data.Booking_id,data.Flightno,data.Extra_Baggage_Allowance,data.Fare]) 

    return response