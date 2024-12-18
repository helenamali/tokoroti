from django.db import models

class Toko(models.Model):
    id_toko = models.AutoField(primary_key=True)
    nama_toko = models.CharField(max_length=100)
    alamat = models.TextField()
    stok_roti = models.IntegerField()

    class Meta:
        verbose_name_plural = 'Toko'

    def __str__(self):
        return self.nama_toko

class Roti(models.Model):
    id_roti = models.AutoField(primary_key=True)
    nama_roti = models.CharField(max_length=100)
    varian_rasa = models.CharField(max_length=50)
    harga = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        verbose_name_plural = 'Roti'

    def __str__(self):
        return self.nama_roti

class Pengunjung(models.Model):
    id_pengunjung = models.AutoField(primary_key=True)
    nama_depan = models.CharField(max_length=50)
    nama_belakang = models.CharField(max_length=50)
    pekerjaan = models.CharField(max_length=100)
    # Tambahkan relasi ke Toko jika pengunjung terhubung langsung dengan toko
    id_toko = models.ForeignKey(Toko, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        verbose_name = "Pengunjung"
        verbose_name_plural = "Pengunjung"

    def __str__(self):
        return f"{self.nama_depan} {self.nama_belakang}"

class Memesan(models.Model):
    id = models.AutoField(primary_key=True)
    id_pengunjung = models.ForeignKey(Pengunjung, on_delete=models.CASCADE)
    jumlah_roti = models.IntegerField()
    totalHarga = models.PositiveIntegerField(verbose_name="Total Harga", default=0)  # Menggunakan default 0

    class Meta:
        verbose_name = "Memesan"
        verbose_name_plural = "Memesan"

    def __str__(self):
        return f"Pesanan {self.id_pengunjung} - Total Harga: {self.totalHarga}"

class DetailMemesan(models.Model):
    id = models.AutoField(verbose_name="idDetail", primary_key=True)
    idMemesan = models.ForeignKey(Memesan, verbose_name="idMemesan", on_delete=models.CASCADE)
    idRoti = models.ForeignKey(Roti, verbose_name="idRoti", on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Detail Memesan"
        verbose_name_plural = "Detail Memesan"

    def __str__(self):
        return f"Pesanan {self.idMemesan} - Roti: {self.idRoti}"

class TokoMemilikiRoti(models.Model):
    id = models.AutoField(primary_key=True)
    id_toko = models.ForeignKey(Toko, on_delete=models.CASCADE)
    jumlah_roti = models.IntegerField(verbose_name="Jumlah Roti")

    class Meta:
        verbose_name = "Toko Memiliki Roti"
        verbose_name_plural = "Toko Memiliki Roti"

    def __str__(self):
        return f"Toko {self.id_toko} - Jumlah Roti: {self.jumlah_roti}"

class DetailTokoRoti(models.Model):
    id = models.AutoField(verbose_name="idDetail", primary_key=True)
    idTokoRoti = models.ForeignKey(TokoMemilikiRoti, verbose_name="idTokoRoti", on_delete=models.CASCADE)
    idRoti = models.ForeignKey(Roti, verbose_name="idRoti", on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Detail Toko Roti"
        verbose_name_plural = "Detail Toko Roti"

    def __str__(self):
        return f"Toko: {self.idTokoRoti.id_toko} - Roti: {self.idRoti.nama_roti}"
