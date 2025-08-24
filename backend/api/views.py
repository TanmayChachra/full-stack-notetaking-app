from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics
from .serializers import UserSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny

# Create your views here.

# View to create new user
class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()       #all create user to access all users so no entry is created if existing entry already exists
    serializer_class = UserSerializer             
    permission_classes = [AllowAny]     #allow anyone (even if not authenticated) to create a new user
