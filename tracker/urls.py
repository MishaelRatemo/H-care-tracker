from django.urls import  path, include
from . import views
from rest_framework import routers
# from .views import UserViewSet


router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)

urlpatterns = [
    
    path('', views.home, name='index'),  
    path('api/', include(router.urls)),  
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('getusers/', views.get_user),  
    path('items/', views.items), 
    path('api/userdetails/<int:pk>',views.user_details),
    path('save_user/', views.save_user),
    path('accounts/profile/', views.profile, name='profile'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    
    # path('allusers/',UserViewSet.as_view(), name='users'),
    
]