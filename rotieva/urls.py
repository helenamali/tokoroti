"""
URL configuration for rotieva project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# urls.py
from django.contrib import admin
from django.urls import path, include
from pesanan.views import roti_terlaris, home, tentang, toko_terjual_tertinggi, kontak, roti_terjual_tertinggi, pengunjung_terbanyak

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),  # Halaman Home diakses dengan URL '/'
    path('tentang/', tentang, name='tentang'),
    path('roti-terlaris/', roti_terlaris, name='roti_terlaris'),
    path('kontak/', kontak, name='kontak'),
    # URL untuk Laporan Roti dengan Penjualan Tertinggi
    path('laporan/roti-penjualan-tertinggi/', roti_terjual_tertinggi, name='roti_terjual_tertinggi'),
    
    # URL untuk Laporan Toko dengan Penjualan Tertinggi
    path('laporan/toko-penjualan-tertinggi/', toko_terjual_tertinggi, name='toko_terjual_tertinggi'),
    
    # URL untuk Laporan Pengunjung dengan Pembelian Tertinggi
    path('laporan/pengunjung-terbanyak/', pengunjung_terbanyak, name='pengunjung_terbanyak'),

]






