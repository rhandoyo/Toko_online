# Generated by Django 2.0 on 2020-04-07 04:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tokopedia', '0005_auto_20200407_0311'),
    ]

    operations = [
        migrations.AddField(
            model_name='barang',
            name='poto',
            field=models.ImageField(default='', upload_to='media/'),
        ),
    ]
