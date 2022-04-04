from django.db import models
from cloudinary.models import CloudinaryField
from django import dispatch
from django.contrib.auth.models import User
from django.db.models.signals import post_save


# Create your models here.
class Hospital(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    hospital_name=models.CharField(max_length=200)
    donor_name=models.CharField(max_length=200)
    item=models.CharField(max_length=200)
    quantity=models.IntegerField()
    address = models.CharField(max_length=100)
    
    