# Generated by Django 4.1.7 on 2023-03-15 22:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_rename_personname_order_person_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='time_to_cook',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Длительность приготовления в часах'),
        ),
    ]
