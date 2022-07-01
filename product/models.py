from django.db import models

CHOICE = (
        ('Available', 'Available'),         # ('Actual Value', 'Human Readable Name')
        ('Not Available', 'Not Available')      # ('Actual Value', 'Human Readable Name')
    )


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
    quantity = models.IntegerField(null=True, blank=True)
    price = models.FloatField()
    count_sold = models.IntegerField(null=True, blank=True)
    status = models.CharField(max_length=50, choices=CHOICE, default='Not Available')
    image = models.ImageField(upload_to="images/")

    def __str__(self):
        return self.name