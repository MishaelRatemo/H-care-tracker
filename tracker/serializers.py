
from django.contrib.auth.models import User
from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):    
    class Meta:
        model = User
        # fields = '__all__'
        fields = ['url', 'username', 'first_name', 'last_name',  'email', 'date_joined']
        
class ProfileSerializers(serializers.ModelSerializer):
    photo=serializers.ImageField(required=False, allow_null=True)
    user= UserSerializer()
    class Meta:
        model = Profile
        fields='__all__'

         
class ItemsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields='__all__'
        
class DonerSerializers(serializers.ModelSerializer):
    class Meta:
        model = Donor
        fields='__all__'

# class HospitalSerializers(serializers.ModelSerializer):
#     class Meta:
#         model = Hospital
#         fields='__all__'
        

# class StoreSerializers(serializers.ModelSerializer):
#     class Meta:
#         model = Hospital
#         fields='__all__'
        