from django.shortcuts import render
from django.http import HttpResponse


def Sign_in(request):
    return render(request, 'Sign.html')
