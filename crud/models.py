from unicodedata import category
from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=256,default="")
    image= models.ImageField(upload_to='prod/images',blank=True,null=True)
    price = models.PositiveSmallIntegerField(default=0)
    brand = models.CharField(max_length=256,default="")
    stock_count = models.PositiveIntegerField(default=0)
    category = models.CharField(max_length=256,default="")
    about = models.CharField(max_length=256,default="")

    def __str__(self):
        return self.name