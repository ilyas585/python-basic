from django.test import TestCase
from online_store.models import Category, Good


class TestViews(TestCase):
    """
    Тест отображаемых страниц
    """
    good_test_name = 'Золофт'
    category_test_name = 'Антидепрессанты'

    def test_index_view(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTrue('object_list' in response.context)

    def test_about_view(self):
        response = self.client.get('/about/')
        self.assertEqual(response.status_code, 200)

    def test_catalog_view(self):
        response = self.client.get('/catalog/')
        self.assertEqual(response.status_code, 200)
        self.assertTrue('object_list' in response.context)

    def test_detail_view(self):
        self.category = Category.objects.create(name=self.category_test_name)
        self.good = Good.objects.create(name=self.good_test_name,
                                        category=self.category,
                                        description='')

        url = f'/good/{self.good.pk}/'

        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
