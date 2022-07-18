from django.db import models
from product.models import Products, validate_negative_value


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
    quantity = models.PositiveIntegerField()
    total_price = models.PositiveIntegerField(blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.vendor)

    class Meta:
        ordering = ['-date']
