from django.forms import formset_factory
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib import messages
from django.utils import timezone
from django.views.generic import ListView

from .forms import AddProduct, OrderItemForm, OrderForm
from .models import OrderItem, Order, Product, Slide


def home(request):
    slides = Slide.objects.all()
    return render(request, 'home_page.html', {'slides': slides})


class ViewProducts(ListView):
    model = Product
    template_name = 'menu.html'
    extra_context = {'title': 'MENU', 'products': Product.objects.all()}


class ViewOrders(ListView):
    model = Order
    template_name = 'orders.html'
    context_object_name = 'orders'
    extra_context = {'title': 'Заказы',
                     'current_status': 0}

    def get_queryset(self):
        return Order.objects.all().order_by('person_name')

    def get(self, request, *args, **kwargs):
        orders = Order.objects.all()
        for order in orders:
            if order.current_status < 100:
                order.update_status()
        return super().get(request, *args, **kwargs)


def order(request):
    OrderItemFormSet = formset_factory(OrderItemForm, extra=5)
    if request.method == 'POST':
        form_items = OrderItemFormSet(request.POST)
        form_name = OrderForm(request.POST)
        if form_items.is_valid() and form_name.is_valid():
            order = Order.objects.create(person_name=form_name.cleaned_data['person_name'])
            print(form_items.cleaned_data)
            for item_form in form_items.cleaned_data:
                try:
                    product = item_form['product']
                    quantity = item_form['quantity']
                    order_item = OrderItem.objects.create(product=product, quantity=quantity, order=order)
                    order_item.update_order()
                except KeyError:
                    pass
            messages.success(request, 'Order was created ! ')
            return redirect('home')
    else:
        form_items = OrderItemFormSet()
        form_name = OrderForm()
    return render(request, 'cart.html', {'form': form_items,
                                         'form_name': form_name})


def add_product(request):
    if request.method == "POST":
        form = AddProduct(request.POST, request.FILES)

        if form.is_valid():
            product = form.save(commit=False)
            product.save()
            messages.success(request, 'Product was added ! ')
            return redirect('home')
    else:
        form = AddProduct()
    return render(request, 'add_product.html', {'form': form,
                                                'title': 'Добавить товар'})
