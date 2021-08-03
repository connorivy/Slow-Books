# Generated by Django 3.2.5 on 2021-08-03 02:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0014_alter_inventory_threshold'),
    ]

    operations = [
        migrations.RenameField(
            model_name='inventory',
            old_name='cost',
            new_name='costper',
        ),
        migrations.AddField(
            model_name='inventory',
            name='value',
            field=models.DecimalField(decimal_places=2, default=111, max_digits=10),
            preserve_default=False,
        ),
    ]