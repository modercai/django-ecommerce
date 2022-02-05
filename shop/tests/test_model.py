from django.test import TestCase
from shop.models import Category, Product
from django.contrib.auth.models import User


'''
using TestCase because Categories is using the database
'''


class TestCategoriesModel(TestCase):

    def setUp(self):
        self.data1 = Category.objects.create(name='django', slug='django')

    '''
        data entry test

    '''

    def test_category_model_entry(self):
        data = self.data1
        self.assertTrue(isinstance(data, Category))

    def test_category_model_entry(self):
        '''
        testing model default name
        '''
        data = self.data1
        self.assertEqual(str(data), 'django')


class TestProductModel(TestCase):
    def setUp(self):
        Category.objects.create(name='django', slug='django')
        User.objects.create(username='admin')
        self.data1 = Product.objects.create(
            category_id=1, title='beginners luck', created_by_id=1, slug='beginners-luck', price='200', image='practice')

    def test_product_model_entry(self):
        '''
        product model insertion test
        '''

        data = self.data1
        self.assertTrue(isinstance(data, Product))
        self.assertEqual(str(data), 'beginners luck')
