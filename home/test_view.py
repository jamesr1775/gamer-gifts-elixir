from django.test import TestCase

# Create your tests here.

class TestHomeView(TestCase):

    # test home page
    def test_home_page(self):
        response = self.client.get('/')
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/index.html')
    # test gift advice page
    def test_gift_advice_page(self):
        response = self.client.get('/gift_advice/')
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/gift_advice.html')
    # test printing info page
    def test_printing_info_page(self):
        response = self.client.get('/printing_info/')
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/printing_info.html')
