from django.shortcuts import render
from django.http import HttpResponse
# 단순히 ㅇ니자로 받은 문자열을 사용자의 화면에 보여 주도록 하는 함수


# Create your views here
def index(request):
    return HttpResponse("my_to_do_app first page")
