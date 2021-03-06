import random

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, get_object_or_404
from basketapp.models import Basket
from mainapp.models import ProductCategory, Product


def get_basket(user):
    if user.is_authenticated:
        return Basket.objects.filter(user=user)
    else:
        return []


def get_hot_product():
    return random.sample(list(Product.objects.all()), 1)[0]


def get_same_products(hot_product):
    same_products = Product.objects.filter(category=hot_product.category).exclude(pk=hot_product.pk)[:4]
    return same_products


def products(request, pk=None, page=1):
    title = 'Каталог'
    links_menu = ProductCategory.objects.all()
    # basket = get_basket(request.user)

    if pk is not None:
        if pk == 0:
            products = Product.objects.filter(
                is_active=True,
                category__is_active=True
            ).order_by('-price')
            category = {'pk': 0, 'name': 'все'}
        else:
            category = get_object_or_404(ProductCategory, pk=pk)
            products = Product.objects.filter(
                category__pk=pk,
                is_active=True,
                category__is_active=True
            ).order_by('-price')

        paginator = Paginator(products, 2)
        try:
            product_paginator = paginator.page(page)
        except PageNotAnInteger:
            product_paginator = paginator.page(1)
        except EmptyPage:
            product_paginator = paginator.page(paginator.num_pages)

        context = {
            'title': title,
            'links_menu': links_menu,
            'category': category,
            'products': product_paginator,
            # 'basket': basket,
        }
        return render(request, 'mainapp/products.html', context)

    hot_product = get_hot_product()
    same_products = get_same_products(hot_product)
    products = Product.objects.filter(
        is_active=True,
        category__is_active=True
    ).order_by('-price')[:2]
    paginator = Paginator(products, 2)
    try:
        product_paginator = paginator.page(page)
    except PageNotAnInteger:
        product_paginator = paginator.page(1)
    except EmptyPage:
        product_paginator = paginator.page(paginator.num_pages)

    context = {
        'title': title,
        'links_menu': links_menu,
        'hot_product': hot_product,
        'same_products': same_products,
        'products': product_paginator,
        # 'basket': basket,
    }

    return render(request, 'mainapp/products.html', context)


def product(request, pk):
    title = 'Товар'
    product = get_object_or_404(Product, pk=pk)

    context = {
        'title': title,
        'links_menu': ProductCategory.objects.all(),
        'product': product,
        'same_products': get_same_products(product),
        # 'basket': get_basket(request.user)
    }
    return render(request, 'mainapp/product.html', context)
