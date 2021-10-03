from django.shortcuts import render


def main(request):
    return render(request, 'my_shop/index.html')


def contacts(request):
    return render(request, 'my_shop/contact.html')
