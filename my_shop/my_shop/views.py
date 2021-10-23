from django.shortcuts import render
from mainapp.models import Product


def main(request):
    title = "Магазин"
    products = Product.objects.all()[:4]
    context = {
        'title': title,
        'products': products,
    }
    return render(request, 'my_shop/index.html', context)


def contacts(request):
    title = "Контакты"
    context = {
        'title': title,
    }
    return render(request, 'my_shop/contact.html', context)
