from django.http import HttpResponse
from django.shortcuts import render

def about(request):
    context_dict = {'boldmessage': 'This tutorial has been put together by Jiahui'}
    return render(request, 'rango/about.html', context=context_dict)

def index(request):
    return render(request, 'rango/index.html')

