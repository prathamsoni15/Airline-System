from django.shortcuts import get_object_or_404,render,redirect
from ..models import FeedbackModel
from django.shortcuts import render
#from ..models import Category as CategoryForm
from ..forms.feedback import FeedbackForm
#from ..models import Category
from django.http import HttpResponse
import csv

def viewFeedback(request):
    context={}
    context["feedbacks"]=FeedbackModel.objects.all()
    return render(request, "feedback/view.html",context)

def addFeedback(request):
    context={}
    form=FeedbackForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect( "viewFeedback")
    context['form']=form
    return render(request,"feedback/add.html",context)

def updateFeedback(request,id):
    context={}
    obj=get_object_or_404(FeedbackModel,id=id)
    form=FeedbackForm(request.POST or None,instance=obj)
    if form.is_valid():
        form.save()
        return redirect("viewFeedback")
    context["form"]=form
    return render(request,"feedback/edit.html",context)

def deleteFeedback(request,id):
    context={}
    obj=get_object_or_404(FeedbackModel,id=id)
    if request.method=="GET":
        obj.delete()
        return redirect("viewFeedback")
    return render(request,"feedback/view.html",context)

def download_Feedbackcsv(request):
    response =HttpResponse('')
    response['Content-Disposition'] = 'attachment; filename=Feedbackdetails.csv'
    writer = csv.writer(response)
    writer.writerow(['Quality_Score','Message'])
    for data in FeedbackModel.objects.all():
        writer.writerow([data.Quality_Score,data.Message]) 

    return response
