# Generated by Django 3.1.7 on 2021-05-17 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_auto_20210516_1834'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='verified',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='offer',
            name='shopSku',
            field=models.CharField(default=1, max_length=255, verbose_name='Ваш SKU'),
            preserve_default=False,
        ),
    ]