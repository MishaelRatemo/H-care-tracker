from email.headerregistry import Address
from django.db import models
from tracker.models import Order
from django.db.models.signals import post_save
from django.contrib.gis.db import models

# Create your models here.
class Hospital(models.Model):
    name=models.CharField(max_length=200)  
    location = models.PointField()
   
    
    
    
class order_status(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    status = models.CharField(max_length=50,default='Pending')
    class Meta:
        db_table= 'order_status'
    
    def __str__(self):
        return self.status