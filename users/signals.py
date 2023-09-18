from django.db.models.signals import post_save
from django.contrib.auth.models import User
from .models import Profile



#sender = model class
#instance = the actual instance is being saved 
#created = checks if it is first time created or already present
def createProfile(sender,instance,created,**kwargs):
    if created:
        Profile.objects.create(
            user=instance,
            username= instance.username,
            email= instance.email
        )


post_save.connect(createProfile,sender=User)
