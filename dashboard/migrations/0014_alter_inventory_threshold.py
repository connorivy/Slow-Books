# Generated by Django 3.2.5 on 2021-08-02 23:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0013_rename_part_invoice_prod'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventory',
            name='threshold',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
