from django.db import models
from django.contrib.auth.models import User


class TimeToEat(models.Model):
    TIME_TO_EAT = (
        ('з', 'завтрак'),
        ('о', 'обед'),
        ('у', 'ужин'),
        ('п', 'перекус'),
        ('оо', 'когда угодно')
    )
    time_to_eat = models.CharField(choices=TIME_TO_EAT, default=3, max_length=2)

    def __str__(self):
        return self.time_to_eat


class Product(models.Model):
    METRICS = (
        ('л', 'миллилитры'),
        ('г', 'граммы'),
        ('шт', 'штуки')
    )
    title = models.CharField(max_length=128)
    description = models.TextField(max_length=1000, default='')
    metric = models.CharField(max_length=2, null=True, choices=METRICS)
    calories = models.FloatField(default=0)
    proteins = models.FloatField(default=0)
    fats = models.FloatField(default=0)
    carbohydrates = models.FloatField(default=0)
    # image = models.ImageField(null=True)

    def __str__(self):
        return self.title


class Receipt(models.Model):
    title = models.CharField(max_length=128)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, default=0)
    description = models.TextField(max_length=1000, default='')
    time_to_eat = models.ManyToManyField(TimeToEat)
    date = models.DateTimeField(auto_now_add=True)
    products = models.ManyToManyField(Product)
    calories = models.FloatField(default=0)
    proteins = models.FloatField(default=0)
    fats = models.FloatField(default=0)
    carbohydrates = models.FloatField(default=0)
    moderation = models.BooleanField(default=False)
    # image = models.ImageField(null=True)

    def __str__(self):
        return self.title


class ReceiptHasProduct(models.Model):
    receipt = models.ForeignKey(Receipt, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    count_of_product = models.PositiveIntegerField(default=0)

    # def __str__(self):
    #     return self.receipt.title


class Fridge(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    how_many = models.PositiveIntegerField(default=0)

    def __str__(self):
        return '%s(%d)'.format(self.product.title, self.how_many)
