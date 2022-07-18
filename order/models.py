from django.contrib.auth.models import User
from django.db import models

from product.models import Products

CHOICE = (
        ('Approved', 'Approved'),          # ('Actual Value', 'Human Readable Name')
        ('Not Approved', 'Not Approved')       # ('Actual Value', 'Human Readable Name')
    )


class Orders(models.Model):
    name = models.CharField(max_length=100)
    status = models.CharField(max_length=50, choices=CHOICE, default='Not Approved')
    total = models.PositiveIntegerField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-date_created']


class OrderDetails(models.Model):
    order = models.ForeignKey(Orders, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Products, on_delete=models.CASCADE, related_name='product')
    quantity = models.PositiveIntegerField()
    price_each = models.PositiveIntegerField()
    total_price = models.PositiveIntegerField()
    discount_price = models.PositiveIntegerField()
    final_price = models.PositiveIntegerField()

    def __str__(self):
        return str(self.user_id)

