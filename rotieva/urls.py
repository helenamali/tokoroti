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
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Rute untuk halaman utama
    path('laporan/roti-terlaris/', views.laporan_roti_terlaris, name='laporan_roti_terlaris'),
    path('laporan/toko-terpopuler/', views.laporan_toko_terpopuler, name='laporan_toko_terpopuler'),
]

