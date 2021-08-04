from django.contrib import admin

from .models import ProductCategory, Product

admin.site.register(ProductCategory)


@admin.register(Product)
class BasketAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'price',
        'quantity',
        'created',
    ]
