from django.test import TestCase, client
from django.shortcuts import get_object_or_404
from products.models import Product, Category
from django.contrib.auth.models import User
from checkout.models import Order, OrderLineItem


class TestCheckoutView(TestCase):

    @classmethod
    def setUp(self):
        category = Category.objects.create(
            name="clothing", friendly_name="Clothing")
        product = Product.objects.create(
                    sku="gg900522",
                    name="Test",
                    category=category,
                    description="A must-have for fans of \
                        the hit Nintendo video game series, \
                            this officially licensed Legend Of Zelda \
                            Runes Mens & Womens T-shirt is the perfect \
                            addition to your gamer wardrobe. Printed \
                            on a black t-shirt, the design \
                            features an awesome lore from the game.",
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

    def test_checkout_page_empty_bag(self):
        response = self.client.get('/checkout/')
        self.assertEquals(response.status_code, 302)

    def test_checkout_page_non_empty_bag(self):
        product = get_object_or_404(Product, name="Test")
        form = {
            'product_quantity': 1,
            'redirect_url': f"/products/{product.id}/",
        }
        response = self.client.post(f'/shopping_bag/add/{product.id}/', form)
        self.assertEqual(response.status_code, 302)
        shopping_bag = self.client.session['shopping_bag']
        response = self.client.get('/checkout/')
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'checkout/checkout.html')

    def test_checkout_page_success(self):
        product = get_object_or_404(Product, name="Test")
        form = {
            'product_quantity': 1,
            'redirect_url': f"/products/{product.id}/",
        }
        response = self.client.post(f'/shopping_bag/add/{product.id}/', form)
        self.assertEqual(response.status_code, 302)
        shopping_bag = self.client.session['shopping_bag']
        form = {
            'full_name': "Test User",
            'email': "Test@Test.com",
            'phone_number': "012345678",
            'street_address1': "Test 1",
            'street_address2': "Test 2",
            'city': "City",
            'county': "Test 3",
            'postcode': "Test 4",
            'country': "IE",
            'stripe_pid': "Test Pid",
            'client_secret': 'Test Secret',
            'save-info': True,
        }
        response = self.client.post('/checkout/', form)
        order = get_object_or_404(Order, full_name="Test User")
        self.assertEquals(response.status_code, 302)
        url = f'/checkout/checkout_success/{order.order_number}'
        self.assertRedirects(response, url)
