from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import *

# Create your views here.

def index(request):
    categories = Category.objects.all()
    # categories에 Category에 담긴 전체를 받아서 저장하고
    content = {'categories': categories}
    # 딕셔너리 형태로 key값을 할당하여
    return render(request, 'shareRes/index.html', content)
    #render를 통해 index에 전달

def restaurantDetail(request):
    #return HttpResponse("restaurantDetail")
    return render(request, 'shareRes/restaurantDetail.html')

def restaurantCreate(request):
    #return HttpResponse("restaurantCreate")
    return render(request, 'shareRes/restaurantCreate.html')

def categoryCreate(request):
    #return HttpResponse("categoryCreate")
    return render(request, 'shareRes/categoryCreate.html')

def Create_category(request):
    category_name = request.POST['categoryName']
    #카테고리 이름을 받아와서 category_name에 저장.
    new_category = Category(category_name = category_name)
    #Category 모델에 대한 객체를 생성
    new_category.save()
    #데이터베이스에 save함수를 이용하여 저장
    return HttpResponseRedirect(reverse('index'))
    #다시 inedx 화면으로 돌아가도록 리턴해준다.