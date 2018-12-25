from django.contrib import admin

# Register your models here.
from .models import *


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'thumbnail', 'position']

    class Meta:
        model = Category


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product)
