# Generated by Django 3.2 on 2021-04-29 11:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='orderitem',
            options={'verbose_name': 'Товар', 'verbose_name_plural': 'Заказанные товары'},
        ),
    ]
