from django.db import models

# Create your models here.

class Product(models.Model):
    title = models.CharField(max_length=200,null=True,blank=True)
    description = models.TextField(null=True,blank=True)
    product_image = models.ImageField(null=True,blank=True)
    price = models.IntegerField(null=True,blank=True)
    status = models.BooleanField(null=True,blank=True) 
    
    def __str__(self) -> str:
        return self.title