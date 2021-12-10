from django.test import TestCase
from django.shortcuts import get_object_or_404
from .models import WishList
from products.models import Product, Category
from profiles.models import UserProfile
from django.contrib.auth.models import User


class TestWishlistModels(TestCase):
    """ Testing the wishlist model """
    @classmethod
    def setUp(self):
        Category.objects.create(
            name="clothing", friendly_name="Clothing")
        Product.objects.create(
                    sku="gg900522",
                    name="Test",
                    description="A must-have for fans of \
                        the hit Nintendo video game series, \
                            this officially licensed Legend Of Zelda \
                            Runes Mens & Womens T-shirt is the perfect \
                            addition to your gamer wardrobe. Printed \
                            on a black t-shirt, the design \
                            features an awesome lore from the game.",
                    has_sizes="True",
                    price=10,
                    product_rating=4.60,
                    product_type="both",
                    products_others_bought="1_1",
                    status="In Stock",
                    image="173849778_bcddebf66e_c.jpg",
            )
        User.objects.create_user(
            'TestUser', 'TestUser@test.com', 'password')

    def test_wishlist_str_method(self):
        """Test string method"""
        user = get_object_or_404(User, username="TestUser")
        user_profile = get_object_or_404(UserProfile, user=user)
        product = get_object_or_404(Product, name="Test")
        item = WishList.objects.create(
            user_profile=user_profile,
            product=product,
        )
        self.assertEqual(str(item), f'{user_profile}\'s Wishlist')
