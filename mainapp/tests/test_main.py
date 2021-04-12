from django.test import TestCase
from django.test.client import Client
from mainapp.models import ProductCategory
from django.core.management import call_command


class TestMainappSmoke(TestCase):

    def setUp(self):
        call_command('flush', '--noinput')
        call_command('loaddata', 'test_db.json')
        self.client = Client()

    def test_mainapp_urls(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

        response = self.client.get('/products/')
        self.assertEqual(response.status_code, 200)

        # проверяем что страницы с категориями открываются
        for category in ProductCategory.objects.all():
            response = self.client.get(f'/products/{category.pk}/')
            self.assertEqual(response.status_code, 200)

    def tearDown(self):
        call_command('sqlsequencereset', 'mainapp', 'authapp', 'ordersapp', 'basket')