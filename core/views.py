# E:/tamrin_kelas/core/views.py

from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def test_page(request):
    return render(request, 'test.html')

def contact_us(request):
    return render(request, 'contact_us.html')
