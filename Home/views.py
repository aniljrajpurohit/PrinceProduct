from django.shortcuts import render
from . import models


# Create your views here.
def home(request):
    categories = models.Category.objects.all()
    return render(request, "Home/index.html", {'categories': categories})
