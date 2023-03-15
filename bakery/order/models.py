from django.db import models


# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название товара")
    timeTiCook = models.IntegerField(verbose_name='Длительность приготовления')

    def __str__(self):
        return f'< Товар: {self.name} >'

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


class Order(models.Model):
    personName = models.CharField(max_length=100, verbose_name="Имя клиента")
    productId = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(verbose_name="Количество товара")

    def __str__(self):
        return f'< Заказ: {self.personName} >'

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

