# Generated by Django 2.0 on 2020-05-09 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tokopedia', '0010_auto_20200509_1033'),
    ]

    operations = [
        migrations.AlterField(
            model_name='barang',
            name='kategory',
            field=models.CharField(choices=[('elektronik', 'elektronik'), ('fashion', 'fashion'), ('olahraga', 'olahraga')], default='elektronik', max_length=50),
        ),
    ]