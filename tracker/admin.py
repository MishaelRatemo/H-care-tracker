from django.contrib import admin
from .models import (
    Hospital,
    Profile,
    Store,
    Item,
    Donor,
    Registrations,
    Order,   
    
)

from. models import  *

# Register your models here.
admin.site.register(Profile)
admin.site.register(Item)
admin.site.register(Store)
admin.site.register(Donor)
admin.site.register(Hospital)
admin.site.register(Registrations)
admin.site.register(Order)


# admin.site.register(Merger)

