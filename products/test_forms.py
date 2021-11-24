from django.test import TestCase
from django.shortcuts import get_object_or_404

from products.models import Category, Product
from .forms import Category, Product
from django.contrib.auth.models import User
from .forms import ProductForm


class TestProductForm(TestCase):
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

    def test_name_field_required(self):
        """Test name field required"""
        product = get_object_or_404(Product, name="Test")
        form = ProductForm({
            'name': '',
        })
        self.assertFalse(form.is_valid())
        self.assertIn('name', form.errors.keys())

    def test_desc_field_required(self):
        product = get_object_or_404(Product, name="Test")
        form = ProductForm({
            'name': 'Test',
            'description': '',
        })
        self.assertFalse(form.is_valid())
        self.assertIn('description', form.errors.keys())

    def test_price_field_required(self):
        product = get_object_or_404(Product, name="Test")
        form = ProductForm({
            'name': 'Test',
            'description': 'Test Description',
            'price': '',
        })
        self.assertFalse(form.is_valid())
        self.assertIn('price', form.errors.keys())

    def test_status_field_required(self):
        product = get_object_or_404(Product, name="Test")
        form = ProductForm({
            'name': 'Test',
            'description': 'Test Description',
            'price': '19.99',
        })
        self.assertFalse(form.is_valid())
        self.assertIn('status', form.errors.keys())


    def test_valid_form(self):
        product = get_object_or_404(Product, name="Test")
        form = ProductForm({
            'name': 'Test',
            'description': 'Test Description',
            'price': '19.99',
            'status': product.status,
        })
        self.assertTrue(form.is_valid())
        self.assertDictEqual({}, form.errors)

    def test_fields_are_explicit_in_form_metaclass(self):
        """Test to check fields in form metaclass"""
        form = ProductForm()
        self.assertEqual([field for field in form.fields ], ['sku', 'name', 'category', 'description', 'has_sizes', 'price', 'product_rating', 'product_type', 'products_others_bought', 'status', 'image'])