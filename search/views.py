from django.shortcuts import render, redirect
from shop.models import Product
from django.db.models import Q


# Create your views here.

def search(request):
    querry = None
    products = None

    if 'q' in request.GET:
        querry = request.GET.get('q')
        products = Product.objects.all().filter(Q(name__contains=querry) | Q(description__contains=querry))
        return render(request, 'search.html', {'querry': querry, 'products': products})
