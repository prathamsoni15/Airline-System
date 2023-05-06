from pyexpat.errors import messages
from django.shortcuts import get_object_or_404,render,redirect
from ..models import CancellationModel
from django.shortcuts import render
#from ..models import Category as CategoryForm
from ..forms.cancellation_form import CancellationForm
from django.http import HttpResponse
import csv
#from ..models import Category

def viewCancel(request):
    context={}
    context["cancels"]=CancellationModel.objects.all()
    return render(request, "cancel/view.html",context)

def addCancel(request):
    context={}
    form=CancellationForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect( "viewCancel")
    context['form']=form
    return render(request,"cancel/add.html",context)

def updateCancel(request,Cancel_id):
    context={}
    obj=get_object_or_404(CancellationModel,Cancel_id=Cancel_id)
    form=CancellationForm(request.POST or None,instance=obj)
    if form.is_valid():
        form.save()
        return redirect("viewCancel")
    context["form"]=form
    return render(request,"cancel/edit.html",context)

def deleteCancel(request,Cancel_id):
    context={}
    obj=get_object_or_404(CancellationModel,Cancel_id=Cancel_id)
    if request.method=="GET":
        obj.delete()
        return redirect("viewCancel")
    return render(request,"cancel/view.html",context)

def download_cancelcsv(request):
    response =HttpResponse('')
    response['Content-Disposition'] = 'attachment; filename=Canceldetails.csv'
    writer = csv.writer(response)
    writer.writerow(['Cancel_id','Booking_id','Cancel_Date','Refund_Money'])
    for data in CancellationModel.objects.all():
        writer.writerow([data.Cancel_id,data.Booking_id,data.Cancel_Date,data.Refund_Money]) 

    return response