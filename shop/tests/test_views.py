from unittest import skip
from shop.models import Product, Category
from django.contrib.auth.models import User
from django.test import TestCase
from django.test import Client
from django.urls import reverse
from django.http import HttpResponse
from shop.views import homePage


class TestViewResponses(TestCase):
    def setUp(self):
        self.c = Client()
        Category.objects.create(name='phones', slug='phones')
        User.objects.create(username='admin')
        self.data1 = Product.objects.create(
            category_id=1, title='beginners luck', created_by_id=1, slug='beginners_luck', price='200', image='practice')

    def test_url_allowed_hosts(self):
        response = self.c.get('/')
        self.assertEqual(response.status_code, 200)

    def test_product_detail_url(self):
        response = self.c.get(
            reverse('shop:product_detail', args=['beginners_luck']))
        self.assertEqual(response.status_code, 200)

    def test_category_list_url(self):
        response = self.c.get(reverse('shop:category_list', args=['phones']))
        self.assertEqual(response.status_code, 200)

    def test_homepage_html(self):
        request = HttpResponse()
        response = homePage(request)
        html = response.content.decode('utf8')
        print(html)
        self.assertEqual(response.status_code, 200)
