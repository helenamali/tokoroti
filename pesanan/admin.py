from django.contrib import admin
from pesanan.models import Toko,Roti,Pengunjung,Memesan,TokoMemilikiRoti, DetailMemesan, DetailTokoRoti

# Register your models here.
admin.site.register(Toko)
admin.site.register(Roti)
admin.site.register(Pengunjung)
admin.site.register(Memesan)
admin.site.register(DetailMemesan)
admin.site.register(TokoMemilikiRoti)
admin.site.register(DetailTokoRoti)