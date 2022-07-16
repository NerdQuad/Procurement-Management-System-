from multiprocessing import context
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .forms import (Product, ProductForm, Supplier, SupplierForm)
# Create your views here.


#procurement officer login
def po_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            #takes user to the menu
            login(request, user)
            return redirect('product')
        else:  
            messages.success(request,("Error Login, Try Again..."))
            return redirect('po_login')
    else: 
        return render(request, 'po_login.html')


#procurement officer registration 
def po_signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ("User registered successfully..."))
            return redirect("po_login")
    else:
        form = UserCreationForm()   
    return render(request, 'po_signup.html', {'form': form, })


#procurement officer logout
def po_logout(request):
    logout(request)
    messages.success(request, ("Logged out successfully..."))
    return redirect('po_login')


#procurement menu
@login_required
def menu(request):
    return render(request, 'menu.html')


#products functionalities
# list of products/services to be purchased by the procurement unit
@login_required
def product(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'product.html', context)

#add products/services to the database
@login_required
def new_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('product')
            except:
                pass
    else:
        form = ProductForm()
    return render(request, 'new_product.html', {'form': form })

#product edit 
def edit_product(request, id):
    products = Product.objects.get(id= id)
    return render(request, 'product_edit.html', {'product': products})


#update product 
def update_product(request, id):
    products = Product.objects.get(id=id)
    form = ProductForm(request.POST, instance= products)
    if form.is_valid():
        form.save()
        return redirect('product')
    return render(request, 'product_update.html', {'products': products})
    


def delete_product(request, id):
    products = Product.objects.get(id = id)
    products.delete()
    return redirect('product')



#purchase request functionalities
@login_required
def purchase_request(request):
    purchase_request = PurchaseRequest.objects.all()
    context = {
        'purchase_request': purchase_request
    }
    return render(request, 'pr.html', context)


@login_required
def create_pr(request):
    return render(request, 'create_pr.html')

#purchase order 
@login_required
def purchase_order(request):
    purchase_orders = PurchaseOrder.objects.all()
    purchase_orders_items = PurchaseOrderItem.objects.all()
    context = {
        'purchase_orders': purchase_orders, 
        'purchase_orders_items': purchase_orders_items
    }
    return render(request, 'po.html', context)
    

#supplier
@login_required
def supplier(request):
    suppliers = Supplier.objects.all()
    context = {
        'suppliers': suppliers
    }
    return render(request, 'supplier.html', context)

@login_required
def new_supplier(request):
    if request.method == "POST":
        form = SupplierForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('supplier')
            except:
                pass 
    else: 
        form = SupplierForm()
    return render(request, 'new_supplier.html', {'form': form})

@login_required
def update_supplier(request, id):
    suppliers = Supplier.objects.get(id = id )
    form = SupplierForm(request.POST, instance=suppliers)
    if form.is_valid():
        form.save()
        return redirect('supplier')
    return render(request, 'supplier_update.html', {'supplier': suppliers})



@login_required 
def edit_supplier(request, id):
    suppliers = Supplier.objects.get(id = id)
    return render(request, 'supplier_edit.html', {'supplier': suppliers})


@login_required
def delete_supplier(request, id):
    suppliers = Supplier.objects.get(id = id)
    suppliers.delete()
    return redirect('supplier')


#Profile
def profile(request):
    return render(request, 'profile.html')

#Home page 
def home(request):
    return render(request, 'home.html')

#Contact page 
def contact(request):
    return render(request, 'contact.html')