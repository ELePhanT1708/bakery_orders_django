from django.forms import forms

from bakery.order.models import Order


class AddOrder(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['personName', 'productId', 'l']
        widgets = {
            'name': forms.TextInput(attrs={"class": "form-control",
                                           "placeholder": "Иван"}),
            'surname': forms.TextInput(attrs={"class": "form-control",
                                              "placeholder": "Павлович"}),
            'last_name': forms.TextInput(attrs={"class": "form-control",
                                                "placeholder": "Смирнов"}),
        }