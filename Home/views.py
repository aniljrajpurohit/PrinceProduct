from django.shortcuts import render

from Home.models import Category


def home(request):
    categories = Category.objects.all()
    return render(request, "Home/index.html", {'categories': categories})
