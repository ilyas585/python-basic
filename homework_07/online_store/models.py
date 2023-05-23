from django.db import models


class Category(models.Model):
    """
    Категории товара
    """
    name = models.CharField(max_length=150, unique=True)

    def __repr__(self):
        return str(self)


class Good(models.Model):
    """
    Товар
    """
    name = models.CharField(max_length=250, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField(blank=True)

    def __repr__(self):
        return str(self)


class Location(models.Model):
    """
    Аптеки
    """
    address = models.CharField(max_length=250, unique=True)

    def __repr__(self):
        return str(self)


class Stock(models.Model):
    """
    Остатки
    """
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    good = models.ForeignKey(Good, on_delete=models.CASCADE)
    qty = models.PositiveIntegerField(null=False)
    price = models.DecimalField(max_digits=5, decimal_places=2, null=False)

    def __repr__(self):
        return str(self)
