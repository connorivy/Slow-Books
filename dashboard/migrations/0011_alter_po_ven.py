# Generated by Django 3.2.5 on 2021-08-02 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0010_po'),
    ]

    operations = [
        migrations.AlterField(
            model_name='po',
            name='ven',
            field=models.CharField(max_length=25),
        ),
    ]
