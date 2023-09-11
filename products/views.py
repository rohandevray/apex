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

