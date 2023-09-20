from django.forms import ModelForm
from django import forms
from .models import Profile


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields =['name','profile_image','contact','email','location',]
        labels ={
            'profile_image':'image',
        }
    
    def __init__(self,*args,**kwargs):
        super(ProfileForm,self).__init__(*args,**kwargs)


