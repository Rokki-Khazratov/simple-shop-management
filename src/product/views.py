from django.shortcuts import render


def index(request):
    
    context = {

    }
    return render(request, 'main/index.html', context)



def all_products(request):
    
    context = {

    }
    return render(request, 'main/all_products.html', context)



def notifacation(request):
    
    context = {

    }
    return render(request, 'main/notifacation.html', context)



def debetors(request):
    
    context = {

    }
    return render(request, 'main/debetors.html', context)




def trade(request):
    
    context = {

    }
    return render(request, 'main/trade.html', context)