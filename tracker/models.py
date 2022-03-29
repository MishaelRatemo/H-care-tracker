from cloudinary.models import CloudinaryField
from django import dispatch
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE )
    photo = CloudinaryField('image')    
    
    def __str__(self):
        return f'{self.user.username} Profile'
    
def create_profile(sender,**kwargs):
        if kwargs['created']:
            user_profile = Profile.objects.create(user=kwargs['instance'])

post_save.connect(create_profile, sender=User)

class Item(models.Model):
    image = CloudinaryField('image')    
    name = models.CharField(max_length=200, null=False, blank=False)
    description = models.TextField(null=True, blank=True)
    price_bought = models.FloatField(default=0)
    reimbursement = models.FloatField(default=0,)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    storages = models.ManyToManyField('Store',  related_name='Storage') 
    
    
class Store(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    item = models.ManyToManyField(Item,  related_name='Items')
    
class Donor(models.Model):
    donor_name=models.CharField(max_length=200)
    dispatch=models.PositiveIntegerField(default=0)
    hospital_name=models.ManyToManyField('Hospital')
    contact = models.CharField(max_length=16)
    price= models.ForeignKey(Item, on_delete=models.CASCADE)
    
    
class Hospital(models.Model):
    hospital_name=models.CharField(max_length=200)
    donor_name=models.ForeignKey(Donor,on_delete=models.CASCADE, max_length=200)
    inventory=models.ForeignKey(Store,on_delete=models.CASCADE,)
    address = models.CharField(max_length=100)
     

   