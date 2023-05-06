from django.http import HttpResponse

def setCookie(request):
    response=HttpResponse("Cookie Set")
    response.set_cookie('key','value')
    return response

def getCookie(request):
    data=request.COOKIES['key']
    return HttpResponse("THis is a Cookie Data"+data)