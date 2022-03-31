from django.urls import  path, include
from . import views
from rest_framework import routers
# from .views import UserViewSet


router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)

urlpatterns = [
    
    path('index/', views.home, name='index'),  
    path('', include(router.urls)),  
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('getusers/', views.get_user),  
    path('items/', views.items), 
    path('save_user/', views.save_user),
    # path('allusers/',UserViewSet.as_view(), name='users'),
    
]