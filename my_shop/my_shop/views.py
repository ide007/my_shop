from django.shortcuts import render
from mainapp.models import Product

header_menu = [
        {'href': '/', 'name': 'Главная'},
        {'href': '/products/', 'name': 'Продукты'},
        {'href': '/contacts/', 'name': 'Контакты'},
        {'href': '/basket/', 'name': 'Корзина'},
]


def main(request):
    title = "Магазин"
    products = Product.objects.all()[:4]
    context = {
        'title': title,
        'products': products,
        'header_menu': header_menu,
    }
    return render(request, 'my_shop/index.html', context)


def contacts(request):
    title = "Контакты"
    context = {
        'title': title,
        'header_menu': header_menu,
    }
    return render(request, 'my_shop/contact.html', context)
