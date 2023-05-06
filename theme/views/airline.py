from django.shortcuts import get_object_or_404,render,redirect
from ..models import AirlineModel
from django.shortcuts import render
#from ..models import Category as CategoryForm
from ..forms.airline_form import AirlineForm
#from ..models import Category
from http.client import HTTPResponse
from django.http import HttpResponse
import csv
from django.http import HttpResponse
import csv
from django.contrib import messages

def viewAirline(request):
    context={}
    context["airlines"]=AirlineModel.objects.all()
    return render(request, "airline_book/view.html",context)

def addAirline(request):
    context={}
    form=AirlineForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect( "viewAirline")
    context['form']=form
    return render(request,"airline_book/add.html",context)

def updateAirline(request,Airline_id):
    context={}
    obj=get_object_or_404(AirlineModel,Airline_id=Airline_id)
    form=AirlineForm(request.POST or None,instance=obj)
    if form.is_valid():
        form.save()
        return redirect("viewAirline")
    context["form"]=form
    return render(request,"airline_book/edit.html",context)

def deleteAirline(request,Airline_id):
    context={}
    obj=get_object_or_404(AirlineModel,Airline_id=Airline_id)
    if request.method=="GET":
        obj.delete()
        return redirect("viewAirline")
    return render(request,"airline_book/view.html",context)

def download_airlinecsv(request):
    response =HttpResponse('')
    response['Content-Disposition'] = 'attachment; filename=airlinedetails.csv'
    writer = csv.writer(response)
    writer.writerow(['Airline_id','From','To','Departing_Date','Returning_Date','Class'])
    for data in AirlineModel.objects.all():
        writer.writerow([data.Airline_id,data.From,data.To,data.Departing_Date,data.Returning_Date,data.Class]) 

    return response

def bulk_upload(request):
    return render(request,"airline_book/bulkUpload.html")

def upload_csv(request):
    if("GET" == request.method):
        return HTTPResponse("Not Valid method")
    csv_file=request.FILES["csv_file"]
    if not csv_file.name.endswith('.csv'):
        return HTTPResponse("File not valid")
    if csv_file.multiple_chunks():
        return HTTPResponse("Upload file is big")
    file_data = csv_file.read().decode("utf-8")
    lines = file_data.split("\n")
    c=len(lines)
    # return HttpResponse(line[0])
    
    for i in range(0,c-1):
        fields = lines[i].split(",")
        data_dict = {}
        data_dict["Airline_id"] = fields[0]
        data_dict["From"] = fields[1]
        data_dict["To"]= fields[2]
        data_dict["Departing_Date"]= fields[3]
        data_dict["Returning_Date"]= fields[4]
        data_dict["Class"]= fields[5]

        cform=AirlineForm(data_dict)
        if cform.is_valid():

            cform.save()
            messages.error(request,'Successsfully Created.')

    return redirect("viewCategory")

# def download_csv(request):
#     response = HttpResponse('text/csv')
#     response['Content-Disposition'] = 'attachment; filename=Airline.csv'
#     writer = csv.writer(response)
#     writer.writerow(['Airline_id','From','To','Departing_Date','Returning_Date','Class'])
#     for data in AirlineModel.objects.all():
#         writer.writerow([data.Airline_id,data.From,data.To,data.Departing_Date,data.Returning_Date,data.Class])

#     return response