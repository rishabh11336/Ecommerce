from django.http import HttpResponse
from django.shortcuts import render
from .models import Product

productss = Product.objects.all().values('category').distinct()


def index(request):
    products = Product.objects.all()
    return render(request, 'index.html', {'products': products, 'productss': productss})





def productpage(request, id):
    products = Product.objects.get(id=id)
    return render(request, 'product.html', {'products': products, 'productss': productss})


def category(request, category):
    products = Product.objects.filter(category=category).order_by('category')
    return render(request, 'category.html', {'products': products, 'productss': productss})
