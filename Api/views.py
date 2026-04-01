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

from .models import Register
from .serializer import Register_serializer
from .models import Search_data
from .serializer import Search_serializer

class Register_view(generics.ListCreateAPIView):
    queryset=Register.objects.all()
    serializer_class=Register_serializer

class Search_view(generics.ListCreateAPIView):
    queryset=Search_data.objects.all()
    serializer_class=Search_serializer
    filter_backends=[filters.SearchFilter]
    search_fields=['Name','About']
# Create your views here.
