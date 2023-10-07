from django.urls import path
from . import views

urlpatterns = [
    path('',views.homePage,name="home"),
    # path('products/',views.products,name="products"),
    path('product/<str:pk>/',views.product,name="product"),
    path('add-product/',views.addproduct,name="add-product"),
    path('update-product/<str:pk>/',views.updateproduct,name="update-product"),
    path('delete-product/<str:pk>/',views.deleteproduct,name="delete-product"),
    path('update_item/',views.updateItem,name="update_item"),
    path('show_wishlist/',views.showWishlist,name="show_wishlist"),
    path('wishlist/',views.addToWishlist,name="wishlist"),
    path('checkout/',views.checkout,name="checkout"),
    path('payment/',views.payment,name="payment"),
    path('process_order/',views.processOrder,name="process_order"),
]

