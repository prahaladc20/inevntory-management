# Generated by Django 2.2.7 on 2019-11-27 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0004_auto_20191127_1522'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventory',
            name='batch_date',
            field=models.DateField(),
        ),
    ]
