# Generated by Django 3.0.6 on 2020-05-19 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rwfw_main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='rwfw_item_table',
            name='item_head',
            field=models.CharField(default='Manager', max_length=30),
        ),
    ]
