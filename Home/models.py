from django.db import models
from . import utils

upload_path_images = 'media/images/'
upload_path_category = 'media/category/'


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField()
    position = models.IntegerField()
    thumbnail = models.ImageField(upload_to=upload_path_category)

    class Meta:
        ordering = ['position']


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=256)
    description = models.TextField()
    position = models.IntegerField()
    price = models.IntegerField(blank=True, null=True)
