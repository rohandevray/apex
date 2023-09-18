from django.shortcuts import render , HttpResponse , redirect
from django.contrib.auth import authenticate ,login,logout
from .models import Profile
from .forms import ProfileForm
from django.contrib.auth.models import User
# Create your views here.


def loginUser(request):
    if request.method == 'POST':
        username = request.POST['username'].lower()
        password = request.POST['password']


        try:
           user = User.objects.get(username=username)
        except:
           return HttpResponse("ERROR404!")
        
        user = authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect("products")
        else:
            return HttpResponse("login failed!")
    return render(request,"users/login.html")


def logoutUser(request):
    logout(request)
    return redirect("products")


def registerUser(request):
    if request.method =='POST':
        username = request.POST['username'].lower()
        name=request.POST['name']
        email_id= request.POST['email']
        password1 = request.POST['password1']
        password2= request.POST['password2']

        if password1 != password2:
            return HttpResponse("ERROR!")
        else:
            try:
                user=User.objects.get(username=username)
            except:
                user = None
            
            if user is None:
                user = User.objects.create(username=username,password=password1,first_name=name,email=email_id)
                return redirect('login')
    return render(request,"users/register.html")


def userProfile(request):
    user = request.user
    profile = Profile.objects.get(user=user)
    context ={'profile':profile}
    return render(request,"users/profile.html",context)
