from django.urls import path
from apps.product.views import product_search, shop, product, cart, checkout

urlpatterns = [
    path("shop", shop, name='shop'),
    path("product", product, name='product'),
    path("cart", cart, name='cart'),
    path("checkout", checkout, name='checkout'),
    path('search/', product_search, name='product_search'),

]

