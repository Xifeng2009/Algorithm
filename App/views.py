from django.shortcuts import render
from .functions import binarySearch

def index(request): return render(request, 'App/index.html')

def binary_search(request):

    context = {}

    return render(request, 'App/binary_search.html', context)


