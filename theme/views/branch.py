from django.shortcuts import get_object_or_404,render,redirect
from ..models import BranchModel
from django.shortcuts import render
#from ..models import Category as CategoryForm
from ..forms.branch_form import BranchForm
import csv
from django.http import HttpResponse
#from ..models import Category

def viewBranch(request):
    context={}
    context["branches"]=BranchModel.objects.all()
    return render(request, "branch/view.html",context)

def addBranch(request):
    context={}
    form=BranchForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect( "viewBranch")
    context['form']=form
    return render(request,"branch/add.html",context)

def updateBranch(request,branch_code):
    context={}
    obj=get_object_or_404(BranchModel,branch_code=branch_code)
    form=BranchForm(request.POST or None,instance=obj)
    if form.is_valid():
        form.save()
        return redirect("viewBranch")
    context["form"]=form
    return render(request,"branch/edit.html",context)

def deleteBranch(request,branch_code):
    context={}
    obj=get_object_or_404(BranchModel,branch_code=branch_code)
    if request.method=="GET":
        obj.delete()
        return redirect("viewBranch")
    return render(request,"branch/view.html",context)

def download_branchcsv(request):
    response =HttpResponse('')
    response['Content-Disposition'] = 'attachment; filename=airlinedetails.csv'
    writer = csv.writer(response)
    writer.writerow(['Branch_code','Add1','Add2','City','Telephone'])
    for data in BranchModel.objects.all():
        writer.writerow([data.Branch_code,data.Add1,data.Add2,data.City,data.Telephone]) 

    return response