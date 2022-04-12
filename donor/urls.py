from django.urls import  path, include
from . import views

urlpatterns = [
    path('', views.donarpage, name='donorhomepg'),
    path('dispatch/<int:id>', views.makepending, name='dispatch'),
    path('rejectreq/<int:id>', views.rejectreq, name='rejectreq'),
        
]