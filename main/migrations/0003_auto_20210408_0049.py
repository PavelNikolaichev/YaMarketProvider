# Generated by Django 3.1.7 on 2021-04-07 21:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20210330_1613'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weightdimension',
            name='offer',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='weightDimensions', to='main.offer'),
        ),
    ]