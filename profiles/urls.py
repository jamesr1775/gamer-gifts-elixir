from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name='profile'),
    path(
        'get_order_history/<order_number>',
        views.get_order_history, name='get_order_history'),
]
