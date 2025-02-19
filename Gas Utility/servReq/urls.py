from django.contrib import admin
from django.urls import path
from servReq import views

urlpatterns = [
    path('', views.index, name='index'),
]
