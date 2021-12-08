from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('gift_advice/', views.gift_advice, name='gift_advice'),
]
