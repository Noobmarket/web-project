from django.contrib import admin
from django.urls import path
from blog import views

urlpatterns = [
    path('', views.home, name="blog-home"),
    path('contacti/', views.contacti, name="blog-contacti")
]