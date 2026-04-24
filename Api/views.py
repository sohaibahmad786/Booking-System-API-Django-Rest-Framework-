from django.shortcuts import render
import jwt
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import ListCreateAPIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.authentication import TokenAuthentication,SessionAuthentication
from rest_framework import permissions
from rest_framework import generics,filters
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from datetime import datetime, timedelta
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.db.models import Q

from .models import Register
from .serializer import Register_serializer
from .models import Booking
from .serializer import Booking_serializer

    
class Register_view(generics.ListCreateAPIView):
    serializer_class=Register_serializer
    permission_classes=[AllowAny]
    def get_queryset(self):
        login_user=self.request.user

        if not login_user.is_authenticated:
            return Register.objects.none()

        if login_user.Role=='admin':
            return Register.objects.all()
        else:
            return Register.objects.filter(id=login_user.id)
    
class Register_detail(generics.RetrieveUpdateDestroyAPIView):
    queryset=Register.objects.all()
    serializer_class=Register_serializer
    authentication_classes=[JWTAuthentication,SessionAuthentication]
    permission_classes=[IsAuthenticated]


class Bookinglistview(generics.ListCreateAPIView):
    serializer_class=Booking_serializer
    permission_classes=[IsAuthenticated]

    def get_queryset(self):
        return Booking.objects.filter(user=self.request.user)
    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)

class AvailableSlotView(APIView):
    def get(self,request):
        date=request.GET.get('date')
        booked_times=Booking.objects.filter(date=date).values_list('time',flat=True)
        all_slots=['9:00','10:00','11:00','12:00','1:00','2:00','3:00']
        available=[slot for slot in all_slots if slot not in booked_times]
        
        return Response({
            'available_slot':available
        })

# Create your views here.
