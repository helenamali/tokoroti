# views.py
from turtle import pd
from django.http import HttpResponse
from django.shortcuts import render
from django.db.models import Prefetch
from django.db.models import Count, Sum
from pesanan.models import Toko, Roti, Pengunjung, Memesan, DetailMemesan

from .models import DetailMemesan

def home(request):
    return render(request, 'home.html')

def tentang(request):
    return render(request, 'tentang.html')

def toko_populer(request):
    return render(request, 'toko_populer.html')

def kontak(request):
    return render(request, 'kontak.html')

from .models import DetailMemesan, Memesan, Pengunjung, Toko

# View untuk Laporan Roti Terlaris
def roti_terlaris(request):
    # Prefetch terkait dengan Roti untuk mengurangi query tambahan
    roti_query = Roti.objects.all()
    
    roti_terlaris = (
        DetailMemesan.objects
        .prefetch_related(Prefetch('idRoti', queryset=roti_query))  # Prefetch data roti
        .values('idRoti__nama_roti')  # Ambil nama roti
        .annotate(total_dipesan=Count('idRoti'))  # Hitung jumlah pesanan
        .order_by('-total_dipesan')  # Urutkan berdasarkan jumlah pesanan
    )

    # Kirim data ke template
    return render(request, 'roti_terlaris.html', {'roti_terlaris': roti_terlaris})


# View untuk Laporan Pengunjung dengan Pembelian Tertinggi
def pengunjung_terbanyak(request):
    # Menghitung total pembelian per pengunjung
    pengunjung_terbanyak = (
        Memesan.objects
        .values('id_pengunjung__nama_depan', 'id_pengunjung__nama_belakang')  # Ambil nama pengunjung
        .annotate(total_pembelian=Sum('totalHarga'))  # Hitung total pembelian per pengunjung
        .order_by('-total_pembelian')  # Urutkan berdasarkan total pembelian
    )
    
    # Kirim data ke template
    return render(request, 'pengunjung_terbanyak.html', {'pengunjung_terbanyak': pengunjung_terbanyak})

# View untuk Laporan Roti dengan Penjualan Tertinggi
def roti_terjual_tertinggi(request):
    # Menghitung total pendapatan per roti
    roti_penjualan_tertinggi = (
        DetailMemesan.objects
        .values('idRoti__nama_roti')  # Ambil nama roti
        .annotate(total_pendapatan=Sum('idMemesan__totalHarga'))  # Hitung total pendapatan per roti
        .order_by('-total_pendapatan')  # Urutkan berdasarkan total pendapatan
    )
    
    # Kirim data ke template
    return render(request, 'roti_terjual_tertinggi.html', {'roti_penjualan_tertinggi': roti_penjualan_tertinggi})


def toko_terjual_tertinggi(request):
    # Menghitung total pendapatan per toko melalui pengunjung
    toko_penjualan_tertinggi = (
        Memesan.objects
        .values('id_pengunjung__id_toko__nama_toko')  # Ambil nama toko melalui pengunjung
        .annotate(total_pendapatan=Sum('totalHarga'))  # Hitung total pendapatan per toko
        .order_by('-total_pendapatan')  # Urutkan berdasarkan total pendapatan
    )
    
    # Kirim data ke template
    return render(request, 'toko_terjual_tertinggi.html', {'toko_penjualan_tertinggi': toko_penjualan_tertinggi})
