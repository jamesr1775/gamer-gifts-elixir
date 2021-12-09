from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_shopping_bag, name='view_shopping_bag'),
    path(
        'add/<product_id>/',
        views.add_product_to_bag, name='add_product_to_bag'),
    path('update_bag/<product_id>/', views.update_bag, name='update_bag'),
    path(
        'remove/<product_id>/',
        views.remove_product_from_bag, name='remove_product_from_bag'),
]
