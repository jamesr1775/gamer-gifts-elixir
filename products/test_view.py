from django.test import TestCase
from django.urls import reverse

class TestProductsView(TestCase):

    # test all products view
    def test_products_page(self):
        response = self.client.get(reverse('products'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/products.html')
