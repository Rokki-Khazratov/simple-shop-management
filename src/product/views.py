from django.shortcuts import render
from .models import Product, Debtors

def index(request):
    
    context = {

    }
    return render(request, 'main/index.html', context)



def all_products(request):
    products = Product.objects.all()
    context = {
        'products' : products, 
    }
    return render(request, 'main/all_products.html', context)



def notifacation(request):
    products = Product.objects.filter(quantity__lt = 20)
    context = {
        'products' : products, 
    }
    return render(request, 'main/notifacation.html', context)



def debetors(request):
    debtors = Debtors.objects.all()
    context = {
        'debtors' : debtors
    }
    return render(request, 'main/debetors.html', context)




def trade(request):
    
    context = {

    }
    return render(request, 'main/trade.html', context)