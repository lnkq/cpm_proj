from django.http import HttpResponse
from django.shortcuts import render

from random import randint

def index(request):
    data = {'data' : [randint(1, 100) for _ in range(10)]}
    return render(request, 'random_numbers.html', context=data)