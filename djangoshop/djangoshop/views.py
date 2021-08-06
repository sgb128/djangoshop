from django.shortcuts import render
from mainapp.models import Product
from basketapp.models import Basket

def index(request):
    title = 'магазин'
    products = Product.objects.all()[:3]

    context = {
        'title': title,
        'products': products,
    }
    return render(request, 'djangoshop/index.html', context=context)


def contacts(request):
    return render(request, 'djangoshop/contact.html')
