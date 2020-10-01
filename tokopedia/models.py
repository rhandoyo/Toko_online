from django.db import models

# Create your models here.
class Pemilik(models.Model):
    nama    = models.CharField(max_length=50) 
    alamat  = models.CharField(max_length=50)
    no_hp   = models.CharField(max_length=20, default='')
    email   = models.EmailField(max_length=254,default='test@gmail.com')   

    def __str__(self):
        return self.nama

class Toko(models.Model):
    nama    = models.CharField(max_length=50)
    alamat  = models.CharField(max_length=50)
    pemilik = models.ForeignKey(Pemilik, on_delete=models.CASCADE, related_name='tokos')

    def __str__(self):
        return self.nama

class Barang(models.Model):
    kategory_barang = (
        ('elektronik','elektronik'),
        ('fashion','fashion'),
        ('olahraga','olahraga')
    )
    status_barang  = (
        ('baru','Baru'),
        ('bekas','Bekas')
    )
    nama     = models.CharField(max_length=70)
    jumlah   = models.IntegerField()
    harga    = models.FloatField()
    poto     = models.ImageField(upload_to='images/', height_field=None, width_field=None, max_length=None, default='')  
    kategory = models.CharField(choices=kategory_barang, max_length=50, default='elektronik')
    status   = models.CharField(choices=status_barang, max_length=50, default='baru')
    toko     = models.ForeignKey(Toko, on_delete=models.CASCADE)

    # ,related_name='barangs'

    def __str__(self):
        return self.nama
    