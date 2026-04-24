from rest_framework import serializers
from django.contrib.auth.hashers import make_password, check_password

from .models import Register
from .models import Booking
        
class Register_serializer(serializers.ModelSerializer):
    class Meta:
        model=Register
        fields=['username','Role','email','password','id']
        
    def create(self, validated_data):
        validated_data['password']=make_password(validated_data['password'])
        return super().create(validated_data)


class Booking_serializer(serializers.ModelSerializer):
    class Meta:
        model=Booking
        fields='__all__'
        extra_kwargs={
           'user':{'read_only':True}
        }
            
        extra_kwargs={
            'sender':{'read_only':True}
        }
