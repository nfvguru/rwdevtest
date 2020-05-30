# Generated by Django 3.0.6 on 2020-05-30 11:34

from django.db import migrations, models
import rwfw_utils.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='rwfw_utils_imgdownload',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imgdwn_path', models.CharField(default='/projects', max_length=200)),
                ('imgdwn_name', models.CharField(default='dwnScript', max_length=20)),
                ('json_path', models.FilePathField(match='*.json', path=rwfw_utils.models.jsons_path, recursive=True)),
            ],
        ),
    ]