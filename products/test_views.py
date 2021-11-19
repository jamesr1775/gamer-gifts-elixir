from django.test import TestCase, client
from django.urls import reverse, resolve

from django.shortcuts import get_object_or_404
from .models import Product, Category

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

