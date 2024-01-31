from django.shortcuts import render
from apps.settings.models import Product

# Create your views here.
def product(request, category_id):
    product_all = Product.objects.all()
    if category_id:
        products = Product.objects.filter()
    return render(request, 'product/product.html', locals())


def shop(request):
    return render(request, 'product/shop.html', locals())


def cart(request):
    return render(request, "product/cart.html", locals())


def checkout(request):
    return render(request, "product/checkout.html", locals())