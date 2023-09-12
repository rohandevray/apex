from django.db import models
import uuid
# Create your models here.

class Product(models.Model):
    title = models.CharField(max_length=200,null=True,blank=True)
    description = models.TextField(null=True,blank=True)
    product_image = models.ImageField(null=True,blank=True)
    price = models.IntegerField(null=True,blank=True)
    status = models.BooleanField(null=True,blank=True) 
    created = models.DateTimeField(auto_now_add=True,null=True)
    def __str__(self):
        return self.title
    

class Cart(models.Model):
    #one-to-one with user login 
    title = models.CharField(max_length=200,default="MYCART")
    items = models.ForeignKey(Product,on_delete=models.CASCADE,null=True,blank=True)
    quantity = models.IntegerField(null=True,blank=True,default=0)
    def __str__(self):
        return self.title