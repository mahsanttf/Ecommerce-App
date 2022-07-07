from django.db import models

from product.models import Products, validate_negative_value

CHOICE = (
        ('Approved', 'Approved'),          # ('Actual Value', 'Human Readable Name')
        ('Not Approved', 'Not Approved')       # ('Actual Value', 'Human Readable Name')
    )


class Orders(models.Model):
    name = models.CharField(max_length=100)
    status = models.CharField(max_length=50, choices=CHOICE, default='Approved')
    total = models.IntegerField(null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class OrderDetails(models.Model):
    order = models.ForeignKey(Orders, on_delete=models.CASCADE)
    product = models.ForeignKey(Products, on_delete=models.CASCADE, related_name='product')
    quantity = models.IntegerField(validators=[validate_negative_value])
    price_each = models.IntegerField(null=True, blank=True)
    total_price = models.IntegerField()
    discount_price = models.IntegerField()
    final_price = models.IntegerField()

    def __str__(self):
        return str(self.order_id)

