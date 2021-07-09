from django.shortcuts import render

from mainapp.models import ProductCategory


def products(request, pk=None):
    title = 'Продукты/каталог'

    links_menu = ProductCategory.objects.all()

    context = {
        'title': title,
        'links_menu': links_menu,
    }

    return render(request=request, template_name='mainapp/products.html', context=context)
