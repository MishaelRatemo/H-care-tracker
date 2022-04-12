from django.db import models
from cloudinary.models import CloudinaryField
from django import dispatch
from django.contrib.auth.models import User
from tracker.models import Order
from django.db.models.signals import post_save


# Create your models here.
class Hospital(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    hospital_name=models.CharField(max_length=200)
    donor_name=models.CharField(max_length=200)
    item=models.CharField(max_length=200)
    quantity=models.IntegerField()
    address = models.CharField(max_length=100)
    date_created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    
class order_status(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    status = models.CharField(max_length=50,default='Pending')
    class Meta:
        db_table= 'order_status'
    
    def __str__(self):
        return self.status