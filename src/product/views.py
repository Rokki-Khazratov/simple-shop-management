from django.shortcuts import render, redirect
from .models import Product, Debtors
from .forms import DebetorsForm

def index(request):
    
    context = {

    }
    return render(request, 'main/index.html', context)

    

# def all_products(request):
#     if request.method == 'POST':
#         product_edit = request.POST.getlist('ozgartirish[]')
#         for edit in product_edit:
#             old_name, new_name = edit.split(',')  
#             # touple da qilingan  
#             try:
#                 product = Product.objects.get(name=old_name)  
#                 # Eski nom bilan mahsulotni qidirish
#                 product.name = new_name  
#                 # Yangi nomni qoyish
#                 product.save()  
#             except Product.DoesNotExist:
#                 pass  
#         return redirect('all_products')  
#         # SAHIFANI YANGILASH UCHUN KERAK
#     else:
#         products = Product.objects.all()
#         context = {
#             'products': products,
#         }
#         return render(request, 'main/all_products.html', context)


def all_products(request):
    products = Product.objects.all()
    if request.method == 'POST':
        edited_products = {}
        for product in products:
            new_name = request.POST.get(f'new_name_{product.id}', '')  
            new_quantity = request.POST.get(f'new_quantity_{product.id}', '')  
            new_price = request.POST.get(f'new_price_{product.id}', '')
            if new_name:
                product.name = new_name
            if new_quantity:
                product.quantity = new_quantity
            if new_price:
                product.price = new_price
            edited_products[product.id] = {
                'name': new_name,
                'quantity': new_quantity,
                'price': new_price
            }
            product.save()
        return render(request, 'main/all_products.html', {'products': products, 'edited_products': edited_products})
    context = {
        'products': products,
    }
    return render(request, 'main/all_products.html', context)




def notifacation(request):
    limits = Product.objects.filter( quantity__lt = 20 )
    context = {
        'limits' : limits, 
    }
    return render(request, 'main/notifacation.html', context)

    #status qilish kerak tolang


def debetors(request):
    # qarzdorlar da qoshish url da 


    if request.method == 'Post':
        form = DebetorsForm(request.Post)
        if form.is_valid:
            form.save()
            return redirect
        else:
            form = DebetorsForm


    debtors = Debtors.objects.all()
    context = {
        'debtors' : debtors
    }
    return render(request, 'main/debetors.html', context)




def trade(request):
    
    context = {

    }
    return render(request, 'main/trade.html', context)