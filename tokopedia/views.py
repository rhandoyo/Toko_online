from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Pemilik, Toko, Barang
from django.contrib import messages

# Create your views here.
# Tampilan Home
def home(request):
    semua_barang = Barang.objects.all();   
    context = {
        'judul' :'Home',
        'barang': semua_barang
    }
    
    # membuat pencarian
    if request.method == 'POST':
        cari = request.POST.get('cari')
        caris = Barang.objects.filter(nama__iexact=cari)

        context = {
            'barang':caris
        }
    return render(request,'tokopedia/home.html',context)

def loginView(request):
    context = {
        'judul': 'LOGIN',
    }
      
    if request.method == 'POST':
        username_input = request.POST.get('nama')
        password_input = request.POST.get('password')
        
        user = authenticate(username=username_input, password=password_input)

        if user and user.is_active:
            login(request, user)
            return redirect('tokopedia:home')
        else:
            messages.add_message(request, messages.INFO, 'Username dan Password yang anda masukkan salah')
            return redirect('tokopedia:login')
    
    return render(request,'tokopedia/login.html',context)
# membuat tampilan Logout
def logoutView(request):
    context = {
        'judul':'Logout',
    }
    if request.method == 'POST':
        if request.POST['logout'] == 'keluar':
            logout(request)
            return redirect('tokopedia:home')

    return render(request,'tokopedia/logout.html',context)

# Membuat User baru melalui templates
def daftar(request): 
    context = {
        'judul':'Daftar'
    }
    if request.method == 'POST':
        username_input = request.POST.get('username')
        email_input    = request.POST.get('email')
        password_input = request.POST.get('password')

        print (username_input, email_input)

        data = User.objects.all()
        data = User.objects.create_user(username=username_input, email=email_input, password=password_input)
        data.save()

        return redirect('tokopedia:login')

    return render(request,'tokopedia/daftar.html',context)


def jual(request):
    # Pemiliks = Pemilik.objects.all()
    semua_toko = Toko.objects.all()
    semua_pemilik = Pemilik.objects.all()

    context = {
        'judul':'Jual',
        'toko' : semua_toko,
        'pemilik': semua_pemilik,
    }
    if request.method == 'POST':
        Barang.objects.create(
            nama         = request.POST['nama_barang'],
            jumlah       = request.POST['jumlah_barang'],
            harga        = request.POST['harga_barang'],
            poto         = request.POST['poto'],
            kategory     = request.POST['kategory'],
            status       = request.POST['status'],
            toko_id      = request.POST['toko'], # harus menggunakan keyword id untuk menyimpan
        )
        return redirect('/')
    
    return render(request,'tokopedia/jual.html',context)

def kategory(request, kategory):
    kategory_barang = Barang.objects.filter(kategory=kategory);
    context = {
        'barang':kategory_barang
    }

    if request.method == 'POST':
        cari = request.POST.get('cari')
        caris = Barang.objects.filter(nama__iexact=cari)
        
        context = {
            'barang':caris
        }
    
    return render(request,'tokopedia/home.html',context)















