from distutils.command.upload import upload
from email.mime import image
from statistics import mode
from unicodedata import category, name
from django.db import models
from .category import Category

class Product(models.Model):
    
    name= models.CharField(max_length=50) # Product Name
    price = models.IntegerField(default=0) # Price
    category = models.ForeignKey(Category , on_delete=models.CASCADE , default=1)
    description = models.CharField(max_length=200 , default='')
    image = models.ImageField(upload_to = 'uploads/products/') # PIL library required

