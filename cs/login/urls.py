from django.urls import path, re_path
from django.conf.urls import include
from django.contrib.auth.models import User
# from rest_framework import routers, serilizers, viewsets
from login.views import CustonAuthToken
from login import views

urlpatterns = [
    re_path(r'^', CustonAuthToken.as_view()),
    re_path(r'example_lista2/$', views.ExampleList2.as_view())
]