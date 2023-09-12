from django.shortcuts import render,redirect
from .models import Product
from .forms import ProductForm
# Create your views here.

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
            return redirect('products')
    context ={'form':form}
    return render(request,"products/product-form.html",context)


def deleteproduct(request,pk):
    product=Product.objects.get(id=pk)
    product.delete()
    return redirect('products')


def mycart(request):
    return render(request,"products/cart.html")

def additems(request,pk):
    product = Product.objects.get(id=pk)
    return render(request,"products/quantity-form.html")

def payement(request):
    return render(request,"products/payment.html")