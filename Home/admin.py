from django.contrib import admin

# Register your models here.
from .models import *


class ProductInline(admin.StackedInline):
    model = Product


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'thumbnail', 'position']
    inlines = [ProductInline]

    class Meta:
        model = Category


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product)


def home(*args, **kwargs):
    pass
