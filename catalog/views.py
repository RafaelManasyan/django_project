from django.shortcuts import render
from .models import Product


def main(request):
    return render(request, 'catalog/main.html')


def products_list(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'catalog/products_list.html', context=context)


def product(request, pk):
    product = Product.objects.get(pk=pk)
    context = {
        'product': product
    }
    return render(request, 'catalog/product.html', context)


def contacts(request):
    return render(request, 'catalog/contacts.html')
