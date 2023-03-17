from datetime import datetime

from django.db import models
# Create your models here.
from django.db import models
from django.utils import timezone


class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название товара")
    time_to_cook = models.DecimalField(max_digits=10, decimal_places=2,
                                       verbose_name='Длительность приготовления в часах', default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2,
                                verbose_name='Цена в рублях', default=1)

    def __str__(self):
        return f'< Товар: {self.name} >'

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


class Order(models.Model):
    person_name = models.CharField(max_length=100, verbose_name="Имя клиента")
    created_at = models.DateTimeField(default=timezone.now, verbose_name="Время создания заказа")
    updated_at = models.DateTimeField(default=timezone.now)
    total_price = models.DecimalField(max_digits=10, decimal_places=2,
                                      verbose_name="Сумма заказа в рублях",
                                      default=0)
    total_time = models.DecimalField(max_digits=10, decimal_places=2,
                                     verbose_name="Время приготовления заказа в часах",
                                     default=0)

    def __str__(self):
        return f'< Заказ: {self.person_name} >'

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f'< Товар в заказе {self.order.person_name}: {self.product.name} >'

    def __init__(self, *args, **kwargs):
        super(OrderItem, self).__init__(*args, **kwargs)
        print('<< OrderItem creating >>')

    def update_order(self):
        price = self.product.price * self.quantity
        print(f'<< Price : {price} >>')

        time = self.product.time_to_cook * self.quantity
        print(f'<< Time : {time} >>')
        print('<< Updating time and price for order >>')

        order = Order.objects.get(id=self.order.id)
        print(order)
        print('Total price before update:', order.total_price)
        print('Total time before update:', order.total_time)
        order.total_price += price
        order.total_time += time
        order.updated_at = timezone.now()
        order.save()
        print('Total price after update:', order.total_price)
        print('Total time after update:', order.total_time)

        print('<< DONE >>')

    class Meta:
        verbose_name = 'Товар в заказе'
        verbose_name_plural = 'Товары в заказах'
