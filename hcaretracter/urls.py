"""hcaretracter URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from tracker.views import logout_view
from hospital.views import  hospital_dataset

from users import urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django_registration.backends.activation.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', include('tracker.urls')),
    path('donor/', include('donor.urls')),
    path('hospital/', include('hospital.urls')),    
    path('about/', include('about.urls')),
    path('contact/', include('contact.urls')),
    path('services/', include('services.urls')), 
    path('maps/', include('markers.urls')) , 
    path('logout',logout_view,name="logout"),
    
    path('hospital_data/', hospital_dataset, name='hospitals'),
     
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
