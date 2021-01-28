from django.shortcuts import render
from .models import ProductCategory, Product

# Create your views here.


def index(request):
    context = {
        'title': 'geekShop',
        'categories': ProductCategory.objects.all(),
    }
    return render(request, 'mainapp/index.html', context)


def products(request):

    context = {
        'title': 'geekShop - Каталог',
        'products': Product.objects.all(),
    }
    return render(request, 'mainapp/products.html', context)
