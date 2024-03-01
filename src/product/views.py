from django.shortcuts import render


def index(request):
    
    context = {

    }
    return render(request, 'index.html', context)



def all(request):
    
    context = {

    }
    return render(request, 'barcha.html', context)



def minus(request):
    
    context = {

    }
    return render(request, 'kamayganlar.html', context)

def come(request):
    
    context = {

    }
    return render(request, 'come.html', context)


def deptor(request):
    
    context = {

    }
    return render(request, 'qarzdorlar.html', context)




def trade(request):
    
    context = {

    }
    return render(request, 'savdo.html', context)