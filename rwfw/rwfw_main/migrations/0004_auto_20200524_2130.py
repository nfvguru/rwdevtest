# Generated by Django 3.0.6 on 2020-05-24 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rwfw_main', '0003_rwfw_item_table_item_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rwfw_item_table',
            name='item_order',
            field=models.IntegerField(unique=True),
        ),
    ]
