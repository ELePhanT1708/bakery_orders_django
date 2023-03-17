from django.forms import formset_factory
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import AddProduct, OrderItemForm, OrderForm
from .models import OrderItem, Order, Product


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
            return redirect('order')
    else:
        form_items = OrderItemFormSet()
        form_name = OrderForm()
    return render(request, 'cart.html', {'form': form_items,
                                         'form_name': form_name})


def add_product(request):
    if request.method == "POST":
        form = AddProduct(request.POST)
        if form.is_valid():
            product = Product(name=form.cleaned_data.get('name'),
                              time_to_cook=form.cleaned_data.get('time_to_cook'),
                              price=form.cleaned_data.get('price'),
                              )
            product.save()
            messages.success(request, 'Product was added ! ')
            return redirect('product')
    else:
        form = AddProduct()
    return render(request, 'add_product.html', {'form': form,
                                                'title': 'Добавить товар'})
