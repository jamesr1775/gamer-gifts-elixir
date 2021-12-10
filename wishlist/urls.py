from django.urls import path
from . import views

urlpatterns = [
    path('', views.wishlist, name='wishlist'),
    path('add_product_to_wishlist/<int:product_id>/', views.add_product_to_wishlist, name='add_product_to_wishlist'),
]
