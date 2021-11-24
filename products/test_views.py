from django.test import TestCase, client
from django.urls import reverse, resolve

from django.shortcuts import get_object_or_404
from .models import Product, Category
from django.contrib.auth.models import User

class TestProductsView(TestCase):
    
    @classmethod
    def setUp(self):
        category = Category.objects.create(name="clothing", friendly_name="Clothing")
        product = Product.objects.create(
                    sku="gg900522",
                    name="Test",
                    category=category,
                    description="A must-have for fans of the hit Nintendo video game series, this officially licensed Legend Of Zelda Runes Mens & Womens T-shirt is the perfect addition to your gamer wardrobe. Printed on a black t-shirt, the design features an awesome lore from the game.",
                    has_sizes="True",
                    price=25.99,
                    product_rating=4.60,
                    product_type="both",
                    products_others_bought="1_1",
                    status="In Stock",
                    image="173849778_bcddebf66e_c.jpg",
            )
        user = User.objects.create_user('TestUser', 'TestUser@test.com', 'password')
        admin = User.objects.create_superuser('admin', 'admin@test.com', 'password', )

    # test all products view
    def test_products_page(self):
        response = self.client.get(reverse('products'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/products.html')

    # test all product detail view
    def test_products_detail_view(self):
        """Test product detail view"""
        product = get_object_or_404(Product, name="Test")
        response = self.client.get(f'/products/{product.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "products/product_details.html")

    # test add product redirect not logged in
    def test_add_product_not_logged_in_redirect(self):
        """Test product detail view"""
        response = self.client.get(f'/products/add/')
        url = "/accounts/login/?next=/products/add/"
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, url)

    # test add product redirect logged in
    def test_add_product_logged_in_redirect(self):
        """Test product detail view"""
        loginresponse = self.client.login(
        username='TestUser', password='password')
        self.assertTrue(loginresponse)
        response = self.client.get(f'/products/add/')
        url = "/products/"
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, url)

    # test add product view with superuser
    def test_add_product_superuser_logged_in_redirect(self):
        """Test product detail view"""
        loginresponse = self.client.login(
        username='admin', password='password')
        self.assertTrue(loginresponse)
        response = self.client.get(f'/products/add/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "products/add_product.html")


    # test delete product redirect not logged in
    def test_delete_product_not_logged_in_redirect(self):
        """Test product detail view"""
        product = get_object_or_404(Product, name="Test")
        response = self.client.get(f'/products/delete/{product.id}/')
        url = "/accounts/login/?next=/products/delete/1/"
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, url)

    # test delete product redirect logged in
    def test_delete_product_logged_in_redirect(self):
        """Test product detail view"""
        loginresponse = self.client.login(
        username='TestUser', password='password')
        self.assertTrue(loginresponse)
        product = get_object_or_404(Product, name="Test")
        response = self.client.get(f'/products/delete/{product.id}/')
        url = "/products/"
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, url)

    # test delete product view with superuser
    def test_delete_product_superuser_logged_in_redirect(self):
        """Test product detail view"""
        loginresponse = self.client.login(
        username='admin', password='password')
        self.assertTrue(loginresponse)
        product = get_object_or_404(Product, name="Test")
        response = self.client.get(f'/products/delete/{product.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "products/delete_product.html")

    # test edit product redirect not logged in
    def test_edit_product_not_logged_in_redirect(self):
        """Test product detail view"""
        product = get_object_or_404(Product, name="Test")
        response = self.client.get(f'/products/edit/{product.id}/')
        url = "/accounts/login/?next=/products/edit/1/"
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, url)

    # test edit product redirect logged in
    def test_edit_product_logged_in_redirect(self):
        """Test product detail view"""
        loginresponse = self.client.login(
        username='TestUser', password='password')
        self.assertTrue(loginresponse)
        product = get_object_or_404(Product, name="Test")
        response = self.client.get(f'/products/edit/{product.id}/')
        url = "/products/"
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, url)

    # test edit product view with superuser
    def test_edit_product_superuser_logged_in_redirect(self):
        """Test product detail view"""
        loginresponse = self.client.login(
        username='admin', password='password')
        self.assertTrue(loginresponse)
        product = get_object_or_404(Product, name="Test")
        response = self.client.get(f'/products/edit/{product.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "products/edit_product.html")