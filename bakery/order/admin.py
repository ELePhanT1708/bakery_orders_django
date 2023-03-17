from django.contrib import admin

from .models import Order, Product, Slide

# Register your models here.
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Slide)
