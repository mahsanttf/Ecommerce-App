from django.db import models
from product.models import Products


class Vendor(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=300)
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class Stock(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE, related_name='vendor')
    products = models.ForeignKey(Products, on_delete=models.CASCADE, related_name='products')
    quantity = models.IntegerField()
    total_price = models.FloatField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.vendor)

    class Meta:
        ordering = ['-date']
