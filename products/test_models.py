from django.test import TestCase
from .models import Product, Category


"""Category Model Test"""
class TestCategoryModels(TestCase):
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
    

"""Product Model Test"""
class TestProductModels(TestCase):
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
        self.assertEqual(item.status, 'In Stock > 20')

    def test_product_default_hassizes(self):
        """Test default has sizes"""
        item = Product.objects.create(
            name='Product 2',
            price='35.99',
        )
        self.assertEqual(item.has_sizes, False)
