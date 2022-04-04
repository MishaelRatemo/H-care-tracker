from django.shortcuts import render
from django.contrib.auth.models import User,Group
from rest_framework import  viewsets, permissions, status
from rest_framework.views import APIView
from .serializers import (
                          UserSerializer,ProfileSerializers, 
                          ItemsSerializers, DonerSerializers,
                          HospitalSerializers
                 )
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *
from django.contrib.auth.hashers import  make_password, check_password



# Create your views here.
def home(request):

    return render(request, 'index.html')



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
    # permission_classes =[permissions.IsAuthenticated]
    
    
    
    
@api_view(['GET'])
def get_user(request):
    users= User.objects.all()
    if users:
        serialize=UserSerializer(users, many=True)
        return Response(serialize.data)
    else:
        return Response([])
    
    
@api_view(['GET'])
def items(request):
    items= Item.objects.all()
    if items:
        serialize=UserSerializer(items, many=True)
        return Response(serialize.data)
    else:
        return Response([])
    
@api_view(['POST'])
def save_user(request):
    userdetails = request.data  
    user =userdetails['username']
    fname = userdetails['first_name']
    lname = userdetails['last_name']
    uemail = userdetails['email']    
    passw = userdetails['password'] 
    passw = make_password(passw)
    check_user= User.objects.filter(username=user)   
    if check_user.exists():
        return Response('User already exists, try again')
    else:
        new_user = User(username=user,first_name=fname,last_name=lname,email=uemail, password=passw)
        new_user.save()
        return Response('User added successfully')
    
@api_view(['GET', 'PUT', 'DELETE'])
def user_details(request,pk):
    """
        Retrieve, update or delete user details.
    """
    try:
       profile = Profile.objects.get(pk=pk)
    except Profile.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = ProfileSerializers(profile)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = ProfileSerializers(profile, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        profile.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
