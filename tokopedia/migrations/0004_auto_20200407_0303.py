# Generated by Django 2.0 on 2020-04-07 03:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tokopedia', '0003_pemilik_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='pemilik',
            name='toko',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='barang',
            name='toko',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='barangs', to='tokopedia.Toko'),
        ),
        migrations.AlterField(
            model_name='toko',
            name='pemilik',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tokos', to='tokopedia.Pemilik'),
        ),
    ]
