from django.core.mail import send_mail
from django.http import HttpResponse
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
                'name': each_product.name,
                'description': each_product.description,
                'price': str(each_product.price),
                'amazon_url': str(each_product.amazon_url),
                'image': each_product.image.url
            })
        product_data.append(copy.deepcopy(temp))
    return render(request, "Home/index.html", {'product_data': product_data, 'categories': categories})


def query(request):
    if request.method == 'POST':
        print(request.POST)
        user_name = request.POST.get('name')
        user_mail = request.POST.get('email')
        user_msg = request.POST.get('message')
        user_ph = request.POST.get('phone')
        to_list = [
            ''
        ]
        send_mail(subject="Mail by " + user_name, message="", from_email=user_mail, recipient_list=to_list,
                  fail_silently=False,
                  html_message=user_msg + "<br>" + user_ph)

        return HttpResponse("Success")
