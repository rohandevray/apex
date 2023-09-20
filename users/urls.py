from django.urls import path
from . import views

urlpatterns =[
    path('profile/',views.userProfile,name="profile"),
    path('login/',views.loginUser,name="login"),
    path('register/',views.registerUser,name="register"),
    path('logout/',views.logoutUser,name="logout"),
    path('update_profile/',views.updateProfile,name="update_profile")
]