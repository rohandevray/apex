from django.urls import path
from . import views

urlpatterns = [
    path('',views.products,name="products"),
    path('product/<str:pk>/',views.product,name="product"),
    path('add-product/',views.addproduct,name="add-product"),
]

