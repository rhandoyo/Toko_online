from django.contrib import admin
from .import models
# Register your models here.

admin.site.register(models.Barang)
admin.site.register(models.Toko)
admin.site.register(models.Pemilik)