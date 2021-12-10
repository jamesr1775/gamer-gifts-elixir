from django.test import TestCase
from django.shortcuts import get_object_or_404
from products.models import Product, Category
from django.contrib.auth.models import User


class TestShoppingBagView(TestCase):

    @classmethod
    def setUp(self):
        category = Category.objects.create(
            name="clothing", friendly_name="Clothing")
        Product.objects.create(
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
        User.objects.create_user(
            'TestUser', 'TestUser@test.com', 'password')

    # test all products view
    def test_shopping_bag_page(self):
        response = self.client.get('/shopping_bag/')
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'shopping_bag/shopping_bag.html')

    # test all product detail view
    def test_add_product_to_bag_view(self):
        """Test product detail view"""
        product = get_object_or_404(Product, name="Test")
        form = {
            'product_quantity': 1,
            'redirect_url': f"/products/{product.id}/",
        }
        response = self.client.post(f'/shopping_bag/add/{product.id}/', form)
        self.assertEqual(response.status_code, 302)
        shopping_bag = self.client.session['shopping_bag']
        self.assertEqual(shopping_bag, {f"{product.id}": 1})

    # test all product detail view
    def test_remove_product_from_bag_view(self):
        """Test product detail view"""
        product = get_object_or_404(Product, name="Test")
        form = {
            'product_quantity': 1,
            'redirect_url': f"/products/{product.id}/",
        }
        response = self.client.post(f'/shopping_bag/add/{product.id}/', form)
        self.assertEqual(response.status_code, 302)
        shopping_bag = self.client.session['shopping_bag']
        self.assertEqual(shopping_bag, {f"{product.id}": 1})

        response = self.client.post(
            f'/shopping_bag/remove/{product.id}/', form)
        self.assertEqual(response.status_code, 200)
        shopping_bag = self.client.session['shopping_bag']
        self.assertEqual(shopping_bag, {})
        self.assertTemplateUsed(response, 'shopping_bag/shopping_bag.html')

        # test all product detail view
    def test_update_bag_view(self):
        """Test product detail view"""
        product = get_object_or_404(Product, name="Test")
        form = {
            'product_quantity': 1,
            'redirect_url': f"/products/{product.id}/",
        }
        response = self.client.post(f'/shopping_bag/add/{product.id}/', form)
        self.assertEqual(response.status_code, 302)
        shopping_bag = self.client.session['shopping_bag']
        self.assertEqual(shopping_bag, {f"{product.id}": 1})
        form = {
            'product_quantity': 3,
        }
        response = self.client.post(
            f'/shopping_bag/update_bag/{product.id}/', form)
        self.assertEqual(response.status_code, 200)
        shopping_bag = self.client.session['shopping_bag']
        self.assertEqual(shopping_bag, {f"{product.id}": 3})
        self.assertTemplateUsed(response, 'shopping_bag/shopping_bag.html')

    def test_add_product_size_to_bag_view(self):
        """Test product detail view"""
        product = get_object_or_404(Product, name="Test")
        form = {
            'product_quantity': 1,
            'product_size': 'm',
            'redirect_url': f"/products/{product.id}/",
        }
        response = self.client.post(f'/shopping_bag/add/{product.id}/', form)
        self.assertEqual(response.status_code, 302)
        shopping_bag = self.client.session['shopping_bag']
        self.assertEqual(
            shopping_bag, {f"{product.id}": {'item_with_sizes': {'m': 1}}})
        form = {
            'product_quantity': 2,
            'product_size': 'xs',
            'redirect_url': f"/products/{product.id}/",
        }
        response = self.client.post(f'/shopping_bag/add/{product.id}/', form)
        self.assertEqual(response.status_code, 302)
        shopping_bag = self.client.session['shopping_bag']
        self.assertEqual(
            shopping_bag,
            {f"{product.id}": {'item_with_sizes': {'m': 1, 'xs': 2}}})
