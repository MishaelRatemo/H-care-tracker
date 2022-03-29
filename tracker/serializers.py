from django.contrib.auth.models import User
from rest_framework import serializers
from .models import*

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [ 'username', 'email', 'groups']
        
class ProfileSerializers(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields='__all__'
        
class ItemsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields='__all__'
        
