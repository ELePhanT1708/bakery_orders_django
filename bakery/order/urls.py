from django.urls import path

from .views import order, add_product, home, ViewProducts, ViewOrders

urlpatterns = [
    path('', home, name='home'),
    path('create_order/', order, name='create order'),
    path('orders/', ViewOrders.as_view(), name='orders'),
    path('add_product/', add_product, name='add prodduct'),
    path('products/', ViewProducts.as_view(), name='products'),
]