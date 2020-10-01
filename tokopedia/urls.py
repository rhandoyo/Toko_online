
from django.urls import path
from . import views


app_name = 'tokopedia'

urlpatterns = [
    path('', views.home, name='home'),
    path('login/',views.loginView, name='login'),
    path('logout/',views.logoutView, name='logout'),
    path('daftar/', views.daftar, name='daftar'),
    path('jual/', views.jual, name='jual'),
    path('kategory/<str:kategory>/', views.kategory, name='kategory'),
    # path('cari/',views.cari_barang, name='cari'),
]



