from django.forms import ModelForm
from django import forms
from .models import Product


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields =['title','description','product_image','price','status']
        labels={
            'product_image' : 'image',
        }
    
    def __init__(self,*args,**kwargs):
        super(ProductForm,self).__init__(*args,**kwargs)

        for name,field in self.fields.items():
            field.widget.attrs.update({'class':'input'})
