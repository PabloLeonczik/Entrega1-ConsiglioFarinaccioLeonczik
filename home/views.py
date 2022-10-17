from django.shortcuts import render
# from datetime import datetime

def about_us(request):
    return render(request, 'home/about_us.html', {})

def index(request):
    return render(request, 'home/index.html', {})

def index2(request):
    return render(request, 'home/index2.html', {})