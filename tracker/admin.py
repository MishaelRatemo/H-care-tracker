from django.contrib import admin
from .models import (
    Hospital,
    Profile,
    Store,
    Item,
    Donor,
    
)

# Register your models here.
admin.site.register(Hospital)
admin.site.register(Profile)
admin.site.register(Store)
admin.site.register(Item)
admin.site.register(Donor)

