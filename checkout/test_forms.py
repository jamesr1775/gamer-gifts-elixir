from django.test import TestCase
from .forms import OrderForm


class TestCheckoutForm(TestCase):
    """ Testing the checkout form """

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
        self.assertEqual(
            form.errors['full_name'][0], 'This field is required.')

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
        self.assertEqual(
            form.errors['phone_number'][0], 'This field is required.')

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
        self.assertEqual(
            form.errors['street_address1'][0], 'This field is required.')

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
        self.assertEqual(
            [field for field in form.fields],
            ['full_name',
                'email', 'phone_number',
                'street_address1', 'street_address2',
                'city', 'postcode', 'country',
                'county'])
