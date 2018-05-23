from django.shortcuts import render

from .models import Product


def index(request):
    return render(request, 'index.html')


def product_list(request):
    products = Product.objects.all()
    context = {
        'products': products,
    }
    return render(request, 'product_list.html', context)
