from django.http import HttpResponse
from django.shortcuts import render

def about(request):
    return render(request, 'rango/about.html')

def index(request):
    return render(request, 'rango/index.html')

