from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def sendEmail(request):
    return HttpResponse("sendEmail")
    #일단 sendEmail이 출력되도록 나중에 구현 예정