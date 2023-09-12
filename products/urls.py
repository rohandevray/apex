from django.urls import path
from . import views

urlpatterns = [
    path('',views.products,name="products"),
    path('product/<str:pk>/',views.product,name="product"),
    path('add-product/',views.addproduct,name="add-product"),
    path('update-product/<str:pk>/',views.updateproduct,name="update-product"),
    path('delete-product/<str:pk>/',views.deleteproduct,name="delete-product"),
    path('cart/',views.mycart,name="mycart"),
    path('addcart/<str:pk>/',views.additems,name="addcart")
]

