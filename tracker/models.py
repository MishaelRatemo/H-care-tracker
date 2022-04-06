from cloudinary.models import CloudinaryField
from django import dispatch
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE )
    photo = CloudinaryField('image', null=True)    
    
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
    quantity = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Store(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    item_name= models.CharField(null=True, max_length=50)
    quantity = models.PositiveIntegerField(default=0)
    item_description = models.TextField(null=True, blank=True)
    


class Donor(models.Model):
    donor_name=models.CharField(max_length=200)
    dispatch=models.PositiveIntegerField(default=0)
    contact = models.CharField(max_length=16)
    store= models.ForeignKey(Store, on_delete=models.CASCADE)
    
    
class Hospital(models.Model):
    hospital_name=models.CharField(max_length=255)
    address = models.CharField(max_length=100)
    
     
class Registrations(models.Model):
    DONOR = 'DONOR'
    HOSPITAL = 'HOSPITAL'
    account_type = [
        (DONOR, 'DONOR'),
        (HOSPITAL, 'HOSPITAL'),        
    ]    
    name = models.CharField(max_length=200)
    account_type = models.CharField(choices=account_type, max_length=50)
    email = models.EmailField(max_length=100, unique=True)
    contact = models.CharField(max_length=16)
    password = models.CharField(max_length=300)
    
    class Meta:
        db_table = 'Registrations'
    
    def __str__(self):
        return self.email
    
class Order(models.Model):
    order_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(Registrations, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    item = models.CharField(max_length=200, blank=True)


class Contact(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    subject=models.TextField()
    
    def __str__(self):
        return self.name