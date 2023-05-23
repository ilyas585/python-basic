from django.test import TestCase
from online_store.models import Category, Good, Location, Stock


class TestCategory(TestCase):
    """
    Тест модели Категории товара
    """
    category_test_name = 'Антидепрессанты'

    def setUp(self):
        self.category = Category.objects.create(name=self.category_test_name)

    def test_create(self):
        self.assertEqual(self.category.name, self.category_test_name)

    def test_str(self):
        self.assertEqual(str(self.category.name), self.category_test_name)


class TestGood(TestCase):
    """
    Тест модели Товар
    """
    good_test_name = 'Золофт'
    category_test_name = 'Антидепрессанты'

    def setUp(self):
        self.category = Category.objects.create(name=self.category_test_name)
        self.good = Good.objects.create(name=self.good_test_name,
                                        category=self.category,
                                        description='')

    def test_create(self):
        self.assertEqual(self.good.category.name, self.category_test_name)
        self.assertEqual(self.good.name, self.good_test_name)

    def test_str(self):
        self.assertEqual(str(f"{self.good.name} ({self.category.name})"),
                         f"{self.good_test_name} ({self.category_test_name})")


class TestLocation(TestCase):
    """
    Тест модели Товар
    """
    location_test_address = 'г.Екатеринбург, ул.Военная,д.1а'

    def setUp(self):
        self.location = Location.objects.create(address=self.location_test_address)

    def test_create(self):
        self.assertEqual(self.location.address, self.location_test_address)

    def test_str(self):
        self.assertEqual(str(self.location.address), self.location_test_address)


class TestStock(TestCase):
    """
    Тест модели Остатки
    """
    location_test_address = 'г.Екатеринбург, ул.Военная,д.1а'
    good_test_name = 'Золофт'
    category_test_name = 'Антидепрессанты'
    stock_test_qty = 1
    stock_test_price = 99.99

    def setUp(self):
        self.category = Category.objects.create(name=self.category_test_name)
        self.good = Good.objects.create(name=self.good_test_name,
                                        category=self.category,
                                        description='')
        self.location = Location.objects.create(address=self.location_test_address)
        self.stock = Stock.objects.create(location=self.location,
                                          good=self.good,
                                          qty=self.stock_test_qty,
                                          price=self.stock_test_price)

    def test_create(self):
        self.assertEqual(self.stock.good.category.name, self.category_test_name)
        self.assertEqual(self.stock.location.address, self.location_test_address)
        self.assertEqual(self.stock.good.name, self.good_test_name)
        self.assertEqual(self.stock.qty, self.stock_test_qty)
        self.assertEqual(self.stock.price, self.stock_test_price)

    def test_str(self):
        self.assertEqual(str(f"{self.location.address} ({self.good.name}) - {self.stock.qty} шт"),
                         f"{self.location_test_address} ({self.good_test_name}) - {self.stock_test_qty} шт")
