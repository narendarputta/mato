# Generated by Django 3.1.4 on 2021-01-03 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productapp', '0009_auto_20210103_2106'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='user',
            new_name='user_id',
        ),
        migrations.AlterField(
            model_name='order',
            name='phonenumber',
            field=models.CharField(max_length=100),
        ),
    ]
