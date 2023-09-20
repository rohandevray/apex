from django.shortcuts import render,redirect,HttpResponse
from django.contrib import messages
from .models import Product
from users.models import Profile
from .forms import ProductForm

# Create your views here.


def homePage(request):
    products = Product.objects.all()
    if request.user.is_authenticated:
        user=request.user
        profile = Profile.objects.get(user=user)
    else:
        return redirect("login")
    context ={'profile': profile,'products':products}
    return render(request,"products/home.html",context)

def products(request):
    products = Product.objects.all()
    context ={'products':products}
    return render(request,"products/products.html",context)

def product(request,pk):
    single_product = Product.objects.get(id=pk)
    context={'product':single_product}
    return render(request,"products/single-product.html",context)

def addproduct(request):
    form = ProductForm()
    if request.method == 'POST':
        form = ProductForm(request.POST,request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.save()
            messages.success(request,"Product was added successfully")
            return redirect("products")
    context= {'form':form}
    return render(request,"products/product-form.html",context)


def updateproduct(request,pk):
    product = Product.objects.get(id=pk)
    form =ProductForm(instance=product) 
    # instance=product fills the form with the details already there 
    if request.method == 'POST':
        form = ProductForm(request.POST,request.FILES,instance=product)
        if form.is_valid():
            product = form.save() 
            # as the project is already save we just have to save the form variables
            messages.success(request,"Product was updated successfully!")
            return redirect('products')
    context ={'form':form}
    return render(request,"products/product-form.html",context)


def deleteproduct(request,pk):
    product=Product.objects.get(id=pk)
    product.delete()
    messages.success(request,"Product was deleted successfully!")
    return redirect('products')


def toggle_status(request,pk):
    product = Product.objects.get(id=pk)
    product.active = True
    product.save()
    return redirect('products')

def delete_item(request,pk):
    product = Product.objects.get(id=pk)
    product.active = False
    product.save()
    return redirect('mycart')


def mycart(request):
    products = Product.objects.filter(active=True)
    length = products.__len__()
    context = {'products':products,'length':length}
    return render(request,"products/cart.html",context)


def checkout(request):
    return render(request,"products/checkout.html")

def payment(request):
    return render(request,"products/payment.html")