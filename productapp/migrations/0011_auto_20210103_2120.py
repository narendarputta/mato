# Generated by Django 3.1.4 on 2021-01-03 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productapp', '0010_auto_20210103_2110'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='price',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='order',
            name='total',
            field=models.FloatField(),
        ),
    ]
