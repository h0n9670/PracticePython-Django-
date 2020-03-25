# my_to_do_app > urls.py
from django.urls import path
# url경로 설정
from .import views
# 사용자에게 보여줄 화면을 처리할 함수를 담고있는 사용자모듈

urlpatterns = [
    path('',views.index)
]

