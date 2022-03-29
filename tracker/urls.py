from django.urls import  path, include
from . import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)

urlpatterns = [
    
    path('', views.home, name='index'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('getusers/', views.get_user),   
    path('save_user/', views.save_user),
    
]