from django.urls import  path, include
from . import views

urlpatterns=[
  path('',views.hshome, name='hshome'),
  path('request/',views.hsrequest, name='request'),
  path('services', views.services, name='services')
]