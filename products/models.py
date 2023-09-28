from django.db import models
from users.models import Profile
import uuid
# Create your models here.

class Product(models.Model):
    title = models.CharField(max_length=200,null=True,blank=True)
    description = models.TextField(null=True,blank=True)
    product_image = models.ImageField(null=True,blank=True)
    price = models.IntegerField(null=True,blank=True)
    status = models.BooleanField(null=True,blank=True)
    active = models.BooleanField(null=True,blank=True,default=False) 
    created = models.DateTimeField(auto_now_add=True,null=True)
    def __str__(self):
        return self.title

# CART (WHOLE ORDER)  
class Order(models.Model):
    profile = models.ForeignKey(Profile,null=True,blank=True,on_delete=models.CASCADE)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)
    transaction_id = models.CharField(max_length=100,null=True)
    def __str__(self):
        return str(self.id)


# SINGLE ITEM attached to order/cart
class OrderItem(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE,null=True,blank=True)
    order = models.ForeignKey(Order,on_delete=models.CASCADE,null=True,blank=True)
    quantity = models.IntegerField(null=True,default=0,blank=True)
    item_added = models.DateTimeField(auto_now_add=True)

    @property
    def get_total(self):
        return self.quantity * self.product.price


