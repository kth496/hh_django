from django.db import models


class Item(models.Model):
    # id = models.IntegerField(primary_key=True)
    name = models.TextField()
    price = models.IntegerField()
    gender = models.CharField(max_length=8)
    category = models.CharField(max_length=20)
    ingredients = models.TextField()
    monthlySales = models.IntegerField()
    imageId = models.TextField()


class Ingredients(models.Model):
    name = models.TextField()
    oily = models.CharField(max_length=1)
    dry = models.CharField(max_length=1)
    sensitive = models.CharField(max_length=1)
