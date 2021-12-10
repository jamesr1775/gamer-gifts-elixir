from django.urls import path
from . import views

urlpatterns = [
    path('', views.wishlist, name='wishlist'),
    path(
        'add_product_to_wishlist/<int:product_id>/',
        views.add_product_to_wishlist,
        name='add_product_to_wishlist'),
    path(
        'remove_product_from_wishlist/<int:product_id>/',
        views.remove_product_from_wishlist,
        name='remove_product_from_wishlist'),
]
