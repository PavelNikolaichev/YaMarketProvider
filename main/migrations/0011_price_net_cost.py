# Generated by Django 3.1.7 on 2021-05-10 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_auto_20210509_1051'),
    ]

    operations = [
        migrations.AddField(
            model_name='price',
            name='net_cost',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Себестоимость'),
        ),
    ]