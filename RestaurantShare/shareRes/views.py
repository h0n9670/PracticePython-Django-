from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import *

# Create your views here.

def index(request):
    categories = Category.objects.all()
    # categories에 Category에 담긴 전체를 받아서 저장하고
    restaurants = Restaurant.objects.all()
    content = {'categories': categories, 'restaurants':restaurants}
    # 딕셔너리 형태로 key값을 할당하여
    return render(request, 'shareRes/index.html', content)
    #render를 통해 index에 전달

def restaurantDetail(request, res_id):
    restaurant = Restaurant.objects.get(id = res_id)
    content = {'restaurant':restaurant}
    #return HttpResponse("restaurantDetail")
    return render(request, 'shareRes/restaurantDetail.html',content)

def restaurantCreate(request):
    categories = Category.objects.all()
    content = {'categories' : categories}
    #return HttpResponse("restaurantCreate")
    return render(request, 'shareRes/restaurantCreate.html', content)

def restaurantUpdate(request, res_id):
    categories = Category.objects.all()
    restaurant = Restaurant.objects.get(id = res_id)
    content = {'categories':categories, 'restaurant':restaurant}
    return render(request, 'shareRes/restaurantUpdate.html', content)

def Update_restaurant(request):
    resId = request.POST['resId']
    change_category_id = request.POST['resCategory']
    change_category = Category.objects.get(id = change_category_id)
    change_name = request.POST['resTitle']
    change_link = request.POST['resLink']
    change_content = request.POST['resContent']
    change_keyword = request.POST['resLoc']
    
    before_restaurant = Restaurant.objects.get(id = resId)
    before_restaurant.category = change_category
    before_restaurant.restaurant_name = change_name
    before_restaurant.restaurant_link = change_link
    before_restaurant.restaurant_content = change_content
    before_restaurant.restaurant_keyword = change_keyword
    before_restaurant.save()
    
    return HttpResponseRedirect(reverse('resDetailPage', kwargs={'res_id':resId}))

def Delete_restaurant(request):
    res_id = request.POST['resId']
    restaurant = Restaurant.objects.get(id = res_id)
    restaurant.delete()
    return HttpResponseRedirect(reverse('index'))

def Create_restaurant(request):
    category_id = request.POST['resCategory']
    category = Category.objects.get(id = category_id)
    name = request.POST['resTitle']
    link = request.POST['resLink']
    content = request.POST['resContent']
    keyword = request.POST['resLoc']
    new_res = Restaurant(category=category,restaurant_name=name
                        ,restaurant_link=link , restaurant_content = content, 
                        restaurant_keyword=keyword)
    new_res.save()
    return HttpResponseRedirect(reverse('index'))

def categoryCreate(request):
    categories = Category.objects.all()
    # categories에 Category에 담긴 전체를 받아서 저장하고
    content = {'categories': categories}
    # 딕셔너리 형태로 key값을 할당하여
    return render(request, 'shareRes/categoryCreate.html',content)
    #render를 통해 categoryCreate.html에 전달

def Create_category(request):
    category_name = request.POST['categoryName']
    #카테고리 이름을 받아와서 category_name에 저장.
    new_category = Category(category_name = category_name)
    #Category 모델에 대한 객체를 생성
    new_category.save()
    #데이터베이스에 save함수를 이용하여 저장
    return HttpResponseRedirect(reverse('index'))
    #다시 inedx 화면으로 돌아가도록 리턴해준다.

def Delete_category(request):
    category_id = request.POST['categoryId']
    delete_category = Category.objects.get(id = caegory_id)
    delete_category.delete()
    return HttpResponseRedirect(reverse('cateCreatePage'))

