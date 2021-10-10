from django.shortcuts import render

header_menu = [
        {'href': '/', 'name': 'home'},
        {'href': '/products/', 'name': 'products'},
        {'href': '/contacts/', 'name': 'contacts'},
]


def main(request):
    title = "Магазин"
    context = {
        'title': title,
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
