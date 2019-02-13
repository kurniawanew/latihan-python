from django.shortcuts import render
from .models import Binatang


def daftar_binatang(request):
   return render(request, 'binatang/daftar_binatang.html', {})

def db_binatang(request):
    binatang = Binatang.objects.all()
    return render(request, 'binatang/db_binatang.html', {'animals': binatang})    

def base_binatang(request):
    binatang = Binatang.objects.all()
    return render(request, 'binatang/base_binatang.html', {'binatangs': binatang}) 