# Generated by Django 3.2.5 on 2021-09-19 02:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('karma2', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shippingaddress',
            name='publications',
        ),
        migrations.AddField(
            model_name='shippingaddress',
            name='publications',
            field=models.ManyToManyField(to='karma2.Profile'),
        ),
    ]
