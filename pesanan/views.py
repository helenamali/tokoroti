from django.shortcuts import render
from django.db.models import Count
from pesanan.models import Roti, DetailMemesan, Toko, Memesan

def laporan_roti_toko(request):
    # Query roti terlaris
    roti_terlaris = (
        DetailMemesan.objects
        .values('idRoti__nama_roti')
        .annotate(total_dipesan=Count('idRoti'))
        .order_by('-total_dipesan')
    )

    # Query toko paling sering dikunjungi
    toko_terpopuler = (
        Memesan.objects
        .values('id_pengunjung__toko__nama_toko')
        .annotate(jumlah_transaksi=Count('id_pengunjung'))
        .order_by('-jumlah_transaksi')
    )

    context = {
        'roti_terlaris': roti_terlaris,
        'toko_terpopuler': toko_terpopuler,
    }
    return render(request, 'laporan.html', context)
