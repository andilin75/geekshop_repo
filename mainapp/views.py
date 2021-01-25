from django.shortcuts import render
import json

# Create your views here.


def index(request):
    context = {
        'title': 'geekShop',
    }
    return render(request, 'mainapp/index.html', context)


def products(request):
    with open("mainapp/fixtures/products.json", "r") as read_file:
        products_decoded = json.load(read_file)

    context = {
        'title': 'geekShop - Каталог',
        'products': products_decoded,
    }
    return render(request, 'mainapp/products.html', context)
