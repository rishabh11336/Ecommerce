from django.shortcuts import render
from django.http import HttpResponse


def Cart(request):
    return render(request, 'cart.html')
