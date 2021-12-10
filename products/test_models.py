from django.test import TestCase
from django.shortcuts import get_object_or_404
from .models import Product, Category, Review
from profiles.models import UserProfile
from django.contrib.auth.models import User
from decimal import Decimal


class TestCategoryModels(TestCase):
    """Category Model Test"""
    def test_category_str_method(self):
        """Test string method"""
        item = Category.objects.create(
            name='category_1',
            friendly_name='Category 1',
        )
        self.assertEqual(str(item), 'category_1')

    def test_category_get_friendly_name_method(self):
        """Test get friendly name method"""
        item = Category.objects.create(
            name='category_2',
            friendly_name='Category 2',
        )
        self.assertEqual(item.get_friendly_name(), 'Category 2')


class TestProductModels(TestCase):
    """Product Model Test"""
    def test_product_str_method(self):
        """Test string method"""
        item = Product.objects.create(
            name='Product 1',
            price='33.99',
        )
        self.assertEqual(str(item), 'Product 1')

    def test_product_default_status(self):
        """Test default status"""
        item = Product.objects.create(
            name='Product 2',
            price='35.99',
        )
        self.assertEqual(item.status, 'In Stock')

    def test_product_default_hassizes(self):
        """Test default has sizes"""
        item = Product.objects.create(
            name='Product 2',
            price='35.99',
        )
        self.assertEqual(item.has_sizes, False)


class TestReviewModels(TestCase):
    """Review Model Test"""
    def test_review_str_method(self):
        """Test string method"""
        user = User.objects.create_user(
            'TestUser', 'TestUser@test.com', 'password')
        user_profile = get_object_or_404(UserProfile, user=user)
        product = Product.objects.create(
            name='Product 2',
            price='35.99',
        )
        review = Review.objects.create(
            rating=4.60,
            user_profile=user_profile,
            product=product,
        )
        self.assertEqual(str(review), 'TestUser')

    def test_review_default_rating(self):
        """Test default status"""
        user = User.objects.create_user(
            'TestUser', 'TestUser@test.com', 'password')
        user_profile = get_object_or_404(UserProfile, user=user)
        product = Product.objects.create(
            name='Product 2',
            price='35.99',
        )
        review = Review.objects.create(
            user_profile=user_profile,
            product=product,
        )
        self.assertEqual(review.rating, Decimal('3.0'))
