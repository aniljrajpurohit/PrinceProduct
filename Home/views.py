from django.shortcuts import render

from Home.models import Category
import copy

def home(request):
    categories = Category.objects.all().order_by('position')
    product_data = []
    for each_categoty in categories:
        temp = []
        for each_product in each_categoty.product_set.all():
            temp.append({
                'name':each_product.name,
                'description':each_product.description,
                'price':str(each_product.price),
                'amazon_url':str(each_product.amazon_url),
                'image':each_product.image.url
                })
        product_data.append(copy.deepcopy(temp))
    return render(request, "Home/index.html", {'product_data': product_data,'categories':categories})
