from django.shortcuts import redirect, render
from django.urls import reverse
from django.contrib import messages
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
    if request.method == 'POST':
        ids_to_retrieve = request.POST.getlist('product_id')
        cart = Product.objects.filter(id__in=ids_to_retrieve)

        for product in cart:
            form_quantity = request.POST.get('quantity_' + str(product.id))
            print(form_quantity)
            
            try:
                form_quantity = int(form_quantity)
            except (TypeError, ValueError):
                form_quantity = 0
                print('ERROR: FORM QUANTITY TYPE ERROR!!')
                
            # Update product quantity
            product.quantity -= form_quantity 
            product.save()

        return render(request, 'main/trade.html', {'cart': cart})
    else:
        products = Product.objects.all()
        return render(request, 'main/trade.html', {'products': products})



def delete_product(request, product_id):
    if request.method == 'POST':
        try:
            product = Product.objects.get(id=product_id)
            product.delete()
            messages.success(request, 'Product deleted successfully')
        except Product.DoesNotExist:
            messages.error(request, 'Product not found')
    return redirect(reverse('all_products'))