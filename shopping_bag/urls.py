from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_shopping_bag, name='view_shopping_bag'),
    path('add/<product_id>/', views.add_product_to_bag, name='add_product_to_bag'),
]
