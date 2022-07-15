from django.db import models
from django.core.exceptions import ValidationError

CHOICE = (
        ('Available', 'Available'),         # ('Actual Value', 'Human Readable Name')
        ('Not Available', 'Not Available')      # ('Actual Value', 'Human Readable Name')
    )


def validate_negative_value(value):  # creating a validator function for negative values
    if value <= 0:
        raise ValidationError('Enter positive value')
    else:
        return value


class Brand(models.Model):
    name = models.CharField(max_length=255)
    # description = models.CharField(max_length=200)
    status = models.CharField(max_length=50, choices=CHOICE, default='Not Available')

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=255)
    # description = models.CharField(max_length=200)
    status = models.CharField(max_length=50, choices=CHOICE, default='Not Available')

    def __str__(self):
        return self.name


class Products(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='brand')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category')
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200, null=True)
    code = models.CharField(max_length=100)
    quantity = models.IntegerField(default=0, blank=True, validators=[validate_negative_value])
    price = models.IntegerField(default=0, validators=[validate_negative_value])
    count_sold = models.IntegerField(default=0, blank=True)
    status = models.CharField(max_length=50, choices=CHOICE, default='Not Available')
    image = models.ImageField(upload_to="images/")

    def __str__(self):
        return self.name
