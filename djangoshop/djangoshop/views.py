from django.shortcuts import render
from mainapp.models import Product
from basketapp.models import Basket

def index(request):
    title = 'магазин'
    products = Product.objects.all()[:3]
    basket = []
    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)

    context = {
        'title': title,
        'products': products,
        'basket': basket
    }
    return render(request, 'index.html', context=context)


def contacts(request):
    return render(request, 'contact.html')
