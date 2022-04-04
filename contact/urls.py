from django.urls import  path
from . import views

urlpatterns = [
    path('', views.contact_us, name='about_us')
]