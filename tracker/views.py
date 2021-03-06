from operator import ne
import re
from django.http import HttpResponse

from django.shortcuts import redirect, render
from django.contrib.auth.models import User,Group
from rest_framework import  viewsets, permissions, status
from rest_framework.views import APIView
from .serializers import (
                          UserSerializer,ProfileSerializers, 
                          ItemsSerializers, DonerSerializers,
                          
                 )
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *
from django.contrib.auth.hashers import  make_password, check_password
from tracker.forms import LoginForm, NewsLetterForm, RegistrationForm
from tracker.models import Registrations, NewsLetterRecipients
from .email import  send_welcome_email
from django.http import JsonResponse

# Create your views here.
def home(request):
    loggedin_user =''
    try:
        loggedin_user = request.COOKIES['loggedin']
    except:
        pass
    title= ' Welcome  '
    form = NewsLetterForm()
    # user = loggedin_user
    context ={'user':loggedin_user,
              'title':title, 
              'newsletter': form,
              }
    return render(request, 'index.html', context)

def signup(request):
    loggedin_user =''
    try:
        loggedin_user = request.COOKIES['loggedin']
    except:
        pass
    error = ''
    success = ''
    form = RegistrationForm()
    if request.method == 'POST':
        print('#######################')
        name = request.POST.get('name')
        account_type = request.POST.get('account_type')
        email = request.POST.get('email')
        contact = request.POST.get('contact') 
        address = request.POST.get('address')               
        password = request.POST.get('password')
        pass_hash = make_password(password)
        
        get_user = Registrations.objects.filter(email=email)
        if get_user.exists():
            error = 'user with this email already exists'
            return redirect('signup')
        else:
            new_user = Registrations(name=name, account_type=account_type, email=email, contact=contact, address=address,password=pass_hash)
            new_user.save()
            success = ' User Registered successfully'
        return redirect('login')
        
    context = {
        'form': form,
        'error': error,
        'success': success,
        'user': loggedin_user
    }
    return render(request, 'signupform.html', context)


def login(request):
    loggedin_user =''
    try:
        loggedin_user = request.COOKIES['loggedin']
    except:
        pass
    form = LoginForm()
    error= ''
    if request.method == 'POST':
        username = request.POST.get('email')
        password = request.POST.get('password')
        get_user = Registrations.objects.filter(email=username)
        if get_user.exists():
            get_user = Registrations.objects.get(email=username)
            get_pass = get_user.password
            if check_password(password,get_pass):
                if get_user.account_type == 'DONOR':
                    destination = 'donorhomepg'                    
                else:
                    destination = 'hshome'
                    
                response = redirect(destination)
                response.set_cookie('loggedin',username)
                return response
                
            else:
                error= 'Incorrect password'
                return redirect('login')
        else:
            error ='User with this email does not exist'            
    
    context = {
        'form': form,
        'error':error,
        'user': loggedin_user
    }
    return render(request, 'logins.html', context)

def newsletter(request):
    name = request.POST.get('your_name')
    email = request.POST.get('email')
    
    recipient = NewsLetterRecipients(name=name,email=email)
    recipient.save()
    send_welcome_email(name, email)
    data = {'success': 'You have been successfully added to mailing list'}
    return JsonResponse(data)




def profile(request):
    userprofile= ' Profile'
    user = request.user
    args ={
        'data': userprofile,
        'user': user,
    }
    return render(request, 'profile.html', args)



def logout_view(request):
        # user = request.COOKIES['loggedin']
        response = redirect("index")
        response.delete_cookie('loggedin')
        return response

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

def contact_us(request):
    if request.method=="POST":
        contact=Contact()
        name=request.POST.get('name')
        email=request.POST.get('email')
        subject=request.POST.get('subject') 
        contact.name=name
        contact.email=email
        contact.subject=subject
        contact.save()
        
        return HttpResponse("Thanks for Contacting US")
    return render(request, 'contact_us.html')
