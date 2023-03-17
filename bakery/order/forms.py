import django.forms as forms

from .models import Order, Product, OrderItem


class OrderItemForm(forms.ModelForm):
    product = forms.ModelChoiceField(queryset=Product.objects.all())
    quantity = forms.IntegerField(min_value=1)

    class Meta:
        model = OrderItem
        fields = ('product', 'quantity')


class OrderForm(forms.Form):
    person_name = forms.CharField(max_length=25)


class AddProduct(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={"class": "form-control",
                                           "placeholder": "Круассан"}),
        }
