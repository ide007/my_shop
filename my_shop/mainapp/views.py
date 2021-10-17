from django.shortcuts import render
from mainapp.models import ProductCategory
from my_shop.views import header_menu


def products(request, pk=None):
    title = 'Каталог'
    links_menu = ProductCategory.objects.all()
    print(pk)
    context = {
        'title': title,
        'header_menu': header_menu,
        'links_menu': links_menu,
    }

    return render(request, 'mainapp/products.html', context)
