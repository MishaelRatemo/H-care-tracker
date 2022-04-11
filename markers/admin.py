from django.contrib.gis import admin

from .models import Marker


@admin.register(Marker)
class MarkerAdmin(admin.GISModelAdmin):
    """Marker admin."""

    list_display = ("name", "location")
