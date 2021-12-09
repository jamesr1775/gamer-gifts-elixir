from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('gift_advice/', views.gift_advice, name='gift_advice'),
    path('printing_info/', views.printing_info, name='printing_info'),
]
