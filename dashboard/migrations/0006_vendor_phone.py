# Generated by Django 3.2.5 on 2021-07-31 18:23

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0005_vendor'),
    ]

    operations = [
        migrations.AddField(
            model_name='vendor',
            name='phone',
            field=models.CharField(blank=True, default=None, max_length=16, null=True, unique=True, validators=[django.core.validators.RegexValidator(regex='^\\+?1?\\d{8,15}$')]),
        ),
    ]