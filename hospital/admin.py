
from hospital.models import Hospital
from django.contrib.gis import admin

# Register your models here.
@admin.register(Hospital)
class mapsAdmin(admin.GISModelAdmin):
    list_display = ('name','location')
    
    