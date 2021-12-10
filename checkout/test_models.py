from django.test import TestCase
from checkout.models import Order, OrderLineItem
from django.shortcuts import get_object_or_404
from products.models import Product, Category
from django.contrib.auth.models import User


class TestOrderModels(TestCase):
    """ Testing the checkout order model """
    @classmethod
    def setUp(self):
        Category.objects.create(
            name="clothing", friendly_name="Clothing")
        Product.objects.create(
                    sku="gg900522",
                    name="Test",
                    description="A must-have for fans of \
                        the hit Nintendo video game series, \
                            this officially licensed Legend Of Zelda \
                            Runes Mens & Womens T-shirt is the perfect \
                            addition to your gamer wardrobe. Printed \
                            on a black t-shirt, the design \
                            features an awesome lore from the game.",
                    has_sizes="True",
                    price=10,
                    product_rating=4.60,
                    product_type="both",
                    products_others_bought="1_1",
                    status="In Stock",
                    image="173849778_bcddebf66e_c.jpg",
            )
        User.objects.create_user(
            'TestUser', 'TestUser@test.com', 'password')

    def test_order_str_method(self):
        """Test string method"""
        order = Order.objects.create(
            full_name="Test User",
            email="test@test.com",
            phone_number="012345678",
            street_address1="Test 1",
            street_address2="Test 2",
            city="Test City",
            country="IE",
            order_total=10,
            stripe_pid="Test Pid",)
        self.assertEqual(str(order), str(order.order_number))

    def test_order_update_method(self):
        """Test string method"""
        product = get_object_or_404(Product, name="Test")
        order = Order.objects.create(
            full_name="Test User",
            email="test@test.com",
            phone_number="012345678",
            street_address1="Test 1",
            street_address2="Test 2",
            city="Test City",
            country="IE",
            order_total=10,
            stripe_pid="Test Pid")
        OrderLineItem.objects.create(
            order=order,
            product=product,
            product_size='m',
            quantity=1)
        self.assertEqual(order.order_total, 10)
        self.assertEqual(order.grand_total, 11)
        self.assertEqual(order.delivery_cost, 1)


class TestOrderLineItemModels(TestCase):
    """ Testing the checkout order line item model """
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
                    price=10,
                    product_rating=4.60,
                    product_type="both",
                    products_others_bought="1_1",
                    status="In Stock",
                    image="173849778_bcddebf66e_c.jpg",
            )
        User.objects.create_user(
            'TestUser', 'TestUser@test.com', 'password')

    def test_order_line_item_str_method(self):
        """Test string method"""
        product = get_object_or_404(Product, name="Test")
        order = Order.objects.create(
            full_name="Test User",
            email="test@test.com",
            phone_number="012345678",
            street_address1="Test 1",
            street_address2="Test 2",
            city="Test City",
            country="IE",
            order_total=10,
            stripe_pid="Test Pid")
        order_line_item = OrderLineItem.objects.create(
            order=order,
            product=product,
            product_size='m',
            quantity=1)
        self.assertEqual(
            str(order_line_item),
            f'SKU {product.sku} on order {order.order_number}')
