from django.contrib import admin
from .models import (
    Profile,
    Store,
    Item,
    Donor,
    Registrations,
    Order,   
    NewsLetterRecipients
)

from. models import  *

# Register your models here.
admin.site.register(Profile)
admin.site.register(Item)
admin.site.register(Store)
admin.site.register(Donor)
admin.site.register(Registrations)
admin.site.register(Order)
admin.site.register(NewsLetterRecipients)


# admin.site.register(Merger)

