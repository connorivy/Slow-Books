# Generated by Django 3.2.5 on 2021-08-04 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0004_balancesheet'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='part_ids',
            field=models.CharField(max_length=150),
        ),
    ]
