from django.http import HttpResponse

def setSession(request):
    request.session['key']="your Data"
    return HttpResponse("Session Stored")

def getSession(request):
    if request.session.has_key('key'):
        data=request.session['key']
    return HttpResponse("data is "+data)