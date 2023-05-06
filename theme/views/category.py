from ast import Return
from http.client import HTTPResponse
from django.shortcuts import get_object_or_404,render,redirect
from ..models import CategoryModel
from django.shortcuts import render
#from ..models import Category as CategoryForm
from ..forms.category_form import CategoryForm
#from ..models import Category
from django.http import HttpResponse
import csv
from django.contrib import messages
import logging
logger=logging.getLogger(__name__)

def viewCategory(request):
    context={}
    context["categories"]=CategoryModel.objects.all()
    return render(request, "category/view.html",context)

def addCategory(request):
    context={}
    form=CategoryForm(request.POST or None)
    if form.is_valid():
        form.save()
        # messages.add_message(request,messages.INFO,'Successsfully Created.')
        messages.error(request,'Successsfully Created.')
        logger.warning('Platform is running at risk')
        return redirect( "viewCategory")
    context['form']=form
    return render(request,"category/add.html",context)

def updateCategory(request,id):
    context={}
    obj=get_object_or_404(CategoryModel,id=id)
    form=CategoryForm(request.POST or None,instance=obj)
    if form.is_valid():
        form.save()
        return redirect("viewCategory")
    context["form"]=form
    return render(request,"category/edit.html",context)

def deleteCategory(request,id):
    context={}
    obj=get_object_or_404(CategoryModel,id=id)
    if request.method=="GET":
        obj.delete()
        return redirect("viewCategory")
    return render(request,"category/view.html",context)

def bulk_upload(request):
    return render(request,"category/bulkUpload.html")

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
        data_dict["title"] = fields[0]
        data_dict["description"] = fields[1]

        cform=CategoryForm(data_dict)
        if cform.is_valid():

            cform.save()
            messages.error(request,'Successsfully Created.')

    return redirect("viewCategory")

def download_csv(request):
    response = HttpResponse('')
    response['Content-Disposition'] = 'attachment; filename=category.csv'
    writer = csv.writer(response)
    writer.writerow(['title','description'])
    for data in CategoryModel.objects.all():
        writer.writerow([data.title,data.description])

    return response