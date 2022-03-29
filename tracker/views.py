from django.shortcuts import render
from django.contrib.auth.models import User,Group
from rest_framework import  viewsets, permissions
from .serializers import (
                 UserSerializer,
                 ProfileSerializers, 
                 ItemsSerializers,
                 DonerSerializers,
                 HospitalSerializers
                 )
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *
from django.contrib.auth.hashers import  make_password, check_password



# Create your views here.
def home(request):
    title= ' Welcome'
    context ={ 'title': title}
    return render(request, 'index.html', context)



'''
############################################
***********    API *************************
############################################
'''
class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes =[permissions.IsAdminUser]
    
@api_view(['GET'])
def get_user(request):
    users= User.objects.all()
    if users:
        serialize=UserSerializer(users, many=True)
        return Response(serialize.data)
    else:
        return Response([])
    
@api_view(['POST'])
def save_user(request):
    userdetails = request.data  
    user =userdetails['username']
    passw = userdetails['password'] 
    passw = make_password(passw)
    check_user= User.objects.filter(username=user)   
    if check_user.exists():
        return Response('User already exists, try again')
    else:
        new_user = User(username=user, password=passw)
        new_user.save()
        return Response('User added successfully')
   
