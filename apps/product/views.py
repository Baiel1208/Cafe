from django.shortcuts import render

from apps.settings.models import Product

from .forms import ProductSearchForm


# Create your views here.
def product(request, category_id):
    product_all = Product.objects.all()
    if category_id:
        products = Product.objects.filter()
    return render(request, 'product/product.html', locals())



def product_search(request):
    if request.method == 'GET':
        form = ProductSearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            results = Product.objects.filter(title__icontains=query)
            return render(request, 'product/search_results.html', {'results': results})
    else:
        form = ProductSearchForm()
    return render(request, 'product/product_search.html', {'form': form})



def shop(request):
    return render(request, 'product/shop.html', locals())


def cart(request):
    return render(request, "product/cart.html", locals())


def checkout(request):
    return render(request, "product/checkout.html", locals())