from django.test import TestCase
from django.urls import reverse
from django.shortcuts import get_object_or_404
from .models import WishList
from products.models import Product, Category, Review
from profiles.models import UserProfile
from checkout.models import Order, OrderLineItem
from django.contrib.auth.models import User


class TestProductsView(TestCase):

    @classmethod
    def setUp(self):
        category = Category.objects.create(
            name="clothing", friendly_name="Clothing")
        product = Product.objects.create(
            sku="gg900522",
            name="Test",
            category=category,
            description="A must-have for fans of the hit \
             Nintendo video game series, this officially \
            licensed Legend Of Zelda Runes Mens & Womens \
            T-shirt is the perfect addition to your gamer \
            wardrobe. Printed on a black t-shirt, \
            the design features an awesome lore from the game.",
            has_sizes="True",
            price=25.99,
            product_rating=4.60,
            product_type="both",
            products_others_bought="1_1",
            status="In Stock",
            image="173849778_bcddebf66e_c.jpg",
        )
        user = User.objects.create_user(
            'TestUser', 'TestUser@test.com', 'password')
        user_profile = get_object_or_404(UserProfile, user=user)
        admin = User.objects.create_superuser(
            'admin', 'admin@test.com', 'password', )

    # test wishlist redirect not logged in
    def test_wishlist_not_logged_in_redirect(self):
        """Test wishlist redirect """
        response = self.client.get('/wishlist/')
        url = "/accounts/login/?next=/wishlist/"
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, url)

    # test wishlist page
    def test_wishlist_logged_in_page(self):
        """Test wishlist view """
        loginresponse = self.client.login(
            username='TestUser', password='password')
        self.assertTrue(loginresponse)
        response = self.client.get('/wishlist/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "wishlist/wishlist.html")

    # test add product view with superuser
    def test_add_product_wishlist_not_logged_in_redirect(self):
        """Test add product to wishlist redirect not logged in"""
        product = get_object_or_404(Product, name="Test")
        response = self.client.get(f'/wishlist/add_product_to_wishlist/{product.id}/')
        url = f"/accounts/login/?next=/wishlist/add_product_to_wishlist/{product.id}/"
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, url)

    # test add product to wish list redirect
    def test_add_product_wishlist_logged_in_redirect(self):
        """Test add product to wishlist redirect"""
        loginresponse = self.client.login(
            username='admin', password='password')
        self.assertTrue(loginresponse)
        product = get_object_or_404(Product, name="Test")
        response = self.client.get(f'/wishlist/add_product_to_wishlist/{product.id}/')
        url = f"/products/{product.id}/"
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, url)

    # test remove product not logged in redirect
    def test_remove_product_wishlist_not_logged_in_redirect(self):
        """Test add product to wishlist redirect not logged in"""
        product = get_object_or_404(Product, name="Test")
        response = self.client.get(f'/wishlist/remove_product_from_wishlist/{product.id}/')
        url = f"/accounts/login/?next=/wishlist/remove_product_from_wishlist/{product.id}/"
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, url)

    # test remove product from wish list redirect
    def test_remove_product_wishlist_logged_in_redirect(self):
        """Test add product to wishlist redirect"""
        loginresponse = self.client.login(
            username='admin', password='password')
        self.assertTrue(loginresponse)
        product = get_object_or_404(Product, name="Test")
        response = self.client.get(f'/wishlist/add_product_to_wishlist/{product.id}/')
        url = f"/products/{product.id}/"
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, url)
        response = self.client.get(f'/wishlist/remove_product_from_wishlist/{product.id}/')
        url = "/wishlist/"
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, url)
