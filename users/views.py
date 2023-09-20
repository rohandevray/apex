from django.shortcuts import render , HttpResponse , redirect
from django.contrib.auth import authenticate ,login,logout
from .models import Profile
from .forms import ProfileForm
from django.contrib import messages
from django.contrib.auth.models import User
# Create your views here.


def loginUser(request):
    if request.method == 'POST':
        username = request.POST['username'].lower()
        password = request.POST['password']


        try:
           user = User.objects.get(username=username)
        except:
           messages.error(request,"There is some issue!")
        
        user = authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request,"Logged In Successfully!")
            return redirect("home")
        else:
            messages.error(request,"User is not found!")
    return render(request,"users/login.html")


def logoutUser(request):
    logout(request)
    messages.success(request,"Logged Out successfully!")
    return redirect("home")


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
                messages.info(request,"User was registered")
                return redirect('login')
    return render(request,"users/register.html")


def updateProfile(request):
    user = request.user
    profile = Profile.objects.get(user=user)
    form = ProfileForm(instance=profile)
    if request.method =='POST':
        form = ProfileForm(request.POST,request.FILES,instance=profile)
        if form.is_valid():
            form.save()
            messages.info(request,"Profile was updated!")
            return redirect("profile")
    context={'form':form,'profile':profile}
    return render(request,"users/profile_form.html",context)


def userProfile(request):
    user = None
    if request.user.is_authenticated :
        user =request.user
    else:
        return HttpResponse("go back")
       
    profile = Profile.objects.get(user=user)   
    context ={'profile':profile}
    return render(request,"users/profile.html",context)
