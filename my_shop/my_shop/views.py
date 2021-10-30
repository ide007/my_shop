from django.shortcuts import render
from basketapp.models import Basket
from mainapp.models import Product


def main(request):
    title = "Магазин"
    basket = []
    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)

    products = Product.objects.all()[:4]

    context = {
        'title': title,
        'products': products,
        'basket': basket
    }
    return render(request, 'my_shop/index.html', context)


def contacts(request):
    title = "Контакты"
    basket = []
    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)
    context = {
        'title': title,
        'basket': basket,
    }
    return render(request, 'my_shop/contact.html', context)
