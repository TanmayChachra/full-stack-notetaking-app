from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics
from .serializers import UserSerializer, NoteSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Note

# Create your views here.

# View to create and view notes
class NoteListCreate(generics.ListCreateAPIView):
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        '''Takes no args; Gets all notes written by the user'''
        user = self.request.user    # Gets the user if he is authenticated (Django Magic!)
        return Note.objects.filter(author=user)


    def perform_create(self, serializer):
        '''No args; A way to override inbuilt create function based on our needs'''
        if serializer.is_valid():
            serializer.save(author=self.request.user) # since author was read-only , hence manually passed
        else:
            print(serializer.errors)

class NoteDelete(generics.DestroyAPIView):
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """Delete notes that user owns"""
        user = self.request.user
        return Note.objects.filter(author=user)

# View to create new user
class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()       #all create user to access all users so no entry is created if existing entry already exists
    serializer_class = UserSerializer             
    permission_classes = [AllowAny]     #allow anyone (even if not authenticated) to create a new user
