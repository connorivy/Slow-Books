# Generated by Django 3.2.5 on 2021-08-01 21:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0008_auto_20210801_0116'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='customer',
            field=models.CharField(max_length=25),
        ),
    ]
