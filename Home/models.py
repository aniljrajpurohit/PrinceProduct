from django.db import models
from . import utils

upload_path_images = 'Media/images/'


# upload_path_category = 'Media/category/'


def category_icon_path(instance, filename):
    extension = filename.split('.')
    extension = extension[len(extension) - 1]
    test = instance.name
    name = ''.join(e for e in test if e.isalnum())
    # print(name)
    return 'Media/Categories/{0}/{1}.{2}'.format(name, name, extension)


def product_media_path(instance, filename):
    extension = filename.split('.')
    extension = extension[len(extension) - 1]
    name = instance.name
    name = ''.join(e for e in name if e.isalnum())
    return 'Media/Categories/{0}/{1}/{2}.{3}'.format(''.join(e for e in instance.category.name if e.isalnum()), name,
                                                     name,
                                                     extension.lower())


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField()
    position = models.IntegerField()
    thumbnail = models.ImageField(upload_to=category_icon_path)

    class Meta:
        ordering = ['position']


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=256)
    description = models.TextField()
    position = models.IntegerField()
    price = models.IntegerField(blank=True, null=True)
    image = models.ImageField(upload_to=product_media_path())
