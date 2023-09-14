from django.shortcuts import render
from django.http import HttpResponse

def setcookie(request):
    response=HttpResponse("cookie is set")
    response.set_cookie('dili','dili876@gmail.com')
    return response
def getcookie(request):
    tutorial = request.COOKIES.get('java=tutorial')
    return HttpResponse("java tutorial@:"+str(tutorial))




# Create your views here.
