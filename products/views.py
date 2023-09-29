from django.shortcuts import render,redirect,HttpResponse 
from django.http import JsonResponse
from django.contrib import messages
from .models import Product, Order, OrderItem
from users.models import Profile
from .forms import ProductForm
import json , sys

# Create your views here.


def homePage(request):
    total= 0
    if request.user.is_authenticated:
        user=request.user
        profile = Profile.objects.get(user=user)
    else:
        return redirect("login")
    
    products = Product.objects.all()
    order = Order.objects.get(profile=request.user.profile)
    orderitems = OrderItem.objects.filter(order=order)
    print("products",products)
    print("order",order)
    print("last",orderitems)
    total =0
    for item in orderitems:
        a=item.quantity
        b=item.product.price
        total = total + a*b
    items_count=orderitems.__len__()
    context ={'profile': profile,'products':products,'orderitems':orderitems,'total':total,'items_count':items_count}
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


#updating cart 
def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action= data['action']
    print('productId',productId)
    print('action',action)

    profile = request.user.profile
    product = Product.objects.get(id=productId)
    order,created = Order.objects.get_or_create(profile=profile,complete=False)
    orderItem , created = OrderItem.objects.get_or_create(order=order,product=product)

    if action =='add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action =='remove':
        orderItem.quantity = (orderItem.quantity - 1)
    
    orderItem.save()

    if orderItem.quantity <=0:
        orderItem.delete()


    return JsonResponse('Item was added',safe=False)

# setting the safe parameter to False actually influences JSON to receive any Python Data Type.

def deleteproduct(request,pk):
    product=Product.objects.get(id=pk)
    product.delete()
    messages.success(request,"Product was deleted successfully!")
    return redirect('products')






# def mycart(request):
#     products = Product.objects.filter(active=True)
#     length = products.__len__()
#     context = {'products':products,'length':length}
#     return render(request,"products/cart.html",context)




# def toggle_status(request,pk):
#     product = Product.objects.get(id=pk)
#     product.active = True
#     product.save()
#     return redirect('products')

# def delete_item(request,pk):
#     product = Product.objects.get(id=pk)
#     product.active = False
#     product.save()
#     return redirect('mycart')

def wishlist(request):
    return render(request,"products/wishlist.html")

def checkout(request):
    order = Order.objects.get(profile=request.user.profile)
    orderitems = OrderItem.objects.filter(order=order)
    total =0
    for item in orderitems:
        a=item.quantity
        b=item.product.price
        total = total + a*b
    context={'orderitems':orderitems,'total':total}
    return render(request,"products/checkout.html",context)

# def payment(request):
#     return render(request,"products/payment.html")