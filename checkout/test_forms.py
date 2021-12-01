from django.test import TestCase, client
from checkout.models import Order, OrderLineItem
from django.shortcuts import get_object_or_404
from products.models import Product, Category
from django.contrib.auth.models import User

from .forms import OrderForm


class TestCheckoutForm(TestCase):
    @classmethod
    def setUpTestData(cls):
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

    def test_full_name_is_required(self):
        """Test to check full name is required"""
        form = OrderForm({
            'full_name': '',
            'email': 'test@test.com',
            'phone_number': '012345678',
            'street_address1': 'Test 1',
            'street_address2': 'Test 2',
            'city': 'Test 3',
            'country': 'IE'
        })
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['full_name'][0], 'This field is required.')

    def test_email_is_required(self):
        """Test to check full name is required"""
        form = OrderForm({
            'full_name': 'Test User',
            'email': '',
            'phone_number': '012345678',
            'street_address1': 'Test 1',
            'street_address2': 'Test 2',
            'city': 'Test 3',
            'country': 'IE'
        })
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['email'][0], 'This field is required.')

    def test_phone_number_is_required(self):
        """Test to check full name is required"""
        form = OrderForm({
            'full_name': 'Test User',
            'email': 'test@test.com',
            'phone_number': '',
            'street_address1': 'Test 1',
            'street_address2': 'Test 2',
            'city': 'Test 3',
            'country': 'IE'
        })
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['phone_number'][0], 'This field is required.')

    def test_street_address1_is_required(self):
        """Test to check full name is required"""
        form = OrderForm({
            'full_name': 'Test User',
            'email': 'test@test.com',
            'phone_number': '012345678',
            'street_address1': '',
            'street_address2': 'Test 2',
            'city': 'Test 3',
            'country': 'IE'
        })
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['street_address1'][0], 'This field is required.')

    def test_city_is_required(self):
        """Test to check full name is required"""
        form = OrderForm({
            'full_name': 'Test User',
            'email': 'test@test.com',
            'phone_number': '012345678',
            'street_address1': 'Test 1',
            'street_address2': 'Test 2',
            'city': '',
            'country': 'IE'
        })
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['city'][0], 'This field is required.')

    def test_country_is_required(self):
        """Test to check full name is required"""
        form = OrderForm({
            'full_name': 'Test User',
            'email': 'test@test.com',
            'phone_number': '012345678',
            'street_address1': 'Test 1',
            'street_address2': 'Test 2',
            'city': 'Test 3',
            'country': ''
        })
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['country'][0], 'This field is required.')

    def test_valid_form(self):
        form = OrderForm({
            'full_name': 'Test User',
            'email': 'test@test.com',
            'phone_number': '012345678',
            'street_address1': 'Test 1',
            'street_address2': 'Test 2',
            'city': 'Test 3',
            'country': 'IE'
        })
        self.assertTrue(form.is_valid())
        self.assertDictEqual({}, form.errors)

    def test_fields_are_explicit_in_form_metaclass(self):
        """Test to check fields in form metaclass"""
        form = OrderForm()
        self.assertEqual([field for field in form.fields ], ['full_name', 'email', 'phone_number',
                  'street_address1', 'street_address2',
                  'city', 'postcode', 'country',
                  'county'])