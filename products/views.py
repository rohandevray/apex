from django.shortcuts import render,redirect,HttpResponse 
from django.http import JsonResponse
from django.contrib import messages
from .models import Product, Order, OrderItem , ShippingAddress , Wishlist
from users.models import Profile 
from .forms import ProductForm
from .utils import cartData
import json , datetime
from django.contrib.auth.decorators import login_required


# Create your views here.


def homePage(request):
    total= 0
    products = Product.objects.all()
    if request.user.is_authenticated:
        data = cartData(request)
        profile =request.user.profile
    else:
        return render(request,'products/home.html',{'products':products,'total':total})
    orderitems = data['items']
    total =0
    for item in orderitems:
        a=item.quantity
        b=item.product.price
        total = total + a*b
    items_count=orderitems.__len__()
    context ={'profile': profile,'products':products,'orderitems':orderitems,'total':total,'items_count':items_count}
    return render(request,"products/home.html",context)

# def products(request):
#     products = Product.objects.all()
#     context ={'products':products}
#     return render(request,"products/products.html",context)


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
@login_required(redirect_field_name="login")
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

@login_required(login_url="login")
def addToWishlist(request):
    data = json.loads(request.body)
    product_id = data['productId']
    profile = request.user.profile
    product = Product.objects.get(id=product_id)
    wishlist , created = Wishlist.objects.get_or_create(profile=profile,product=product)
    return JsonResponse('Added to wishlist',safe=False)

def showWishlist(request):
    wishlist = Wishlist.objects.filter(profile=request.user.profile)
    return render(request,"products/wishlist.html",{'wishlist':wishlist})

@login_required(login_url="login")
def checkout(request):
    if request.user.is_authenticated:
        profile = request.user.profile
        data = cartData(request)
    else:
        return render(request,"products/checkout.html")
    orderitems = data['items']
    sub_total =0
    for item in orderitems:
        a=item.quantity
        b=item.product.price
        sub_total = sub_total + a*b
    total = float(sub_total)+float(43.20)
    context={'orderitems':orderitems,'total':total,'sub_total':sub_total}
    return render(request,"products/checkout.html",context)

@login_required(login_url="login")
def payment(request):
    flag=False
    if request.user.is_authenticated:
        profile = request.user.profile
        data = cartData(request)
        flag=True
    else:
        return render(request,"products/payment.html",{'flag':flag})  
    order= data['order']
    return render(request,"products/payment.html",{'flag':flag,'order':order})

def processOrder(request):
    transaction_id = datetime.datetime.now().timestamp()
    data = json.loads(request.body)
    if request.user.is_authenticated:
        profile = request.user.profile
        order,created = Order.objects.get_or_create(profile=profile,complete=False)
        total = float(data['form']['total'])
        order.transaction_id = transaction_id
        if total == order.get_cart_total:
            order.complete = True
        order.save()

        ShippingAddress.objects.create(
            profile =profile,
            order = order,
            address = data['shipping']['address'],
            city = data['shipping']['city'],
            state = data['shipping']['state'],
            zipcode = data['shipping']['zipcode'],
        )
        
    else:
        print("user is not logged in!")
    print('data',data)
    return JsonResponse('payment is done! Thanks for shopping',safe=False)