from django.http import HttpResponse
from django.shortcuts import render,redirect
#from dashboard.models import *
#from userSite.forms import *
#from userSite.models import *
from django.contrib import messages
from ..models import SignUp
from ..forms.Sign_form import SignUpForm

def signup(request):
    return render(request, 'signup/SignUp.html')


def sup(request):  
    username = 'not logged in'  
    if request.method == "POST": 
        form = SignUpForm(request.POST or None) 
        # form.save() 
        #return HttpResponse(request,form)  
        if form.is_valid():
            try:  
                username = form.cleaned_data['username']
                request.session['username'] = username
                form.save()
                messages.success(request, "SuccessFully Register.!!") 
                #return render_to_response('SignUp.html', message='Register complted')
                return render(request,'signup/SignUp.html')  
            except:  
                pass  
    else:  
        form = SignUpForm() 
    return render(request,'signup/SignUp.html',{'form':form})



def loginHandle(request):
    
    if request.method == "POST":    
        form = SignUpForm(request.POST)
        un = request.POST.get("username")
        ps = request.POST.get("password")
        uname = SignUp.objects.all().filter(username=un)
        
       
        if uname[0].username == un and uname[0].password == ps:
            messages.success(request,"SuccessFully Login.!!")
            return render(request,'index1.html',{'username' : un})  
            
            # return HttpResponse('successful')
        
        else:
            messages.error(request, "Username or password not correct..!!")
            return render(request,'signup/SignUp.html', context = {"form":form})
    
    else:
        form = SignUpForm()
        
    return render(request,'signup/SignUp.html', context = {"form":form})

def logout1(request):
    return render(request,'signup/SignUp.html')