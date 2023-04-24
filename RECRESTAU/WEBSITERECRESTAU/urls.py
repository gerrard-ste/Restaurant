from django import views
from django.contrib import admin
from django.urls import path,include
from WEBSITERECRESTAU import views


urlpatterns = [
    path('', views.home, name="home"),
    path('login/', views.login, name="login"),
    path('signup/', views.signup, name="signup")
]