from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import generics
from .serializers import UserSerializer, NoteSerializer
from .models import Note


class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all() # Check if there is similiar user
    serializer_class = UserSerializer # What data to be accept
    permission_classes = [AllowAny] # Give permission to all

class NoteListCreate(generics.ListCreateAPIView):
    serializer_class = NoteSerializer
    permission_classess = [IsAuthenticated] # Just for try use AllowAny to see is it class work

    # Show all notes of the authenticated user
    def get_queryset(self):
        user = self.request.user    # ask which is the user
        return Note.objects.filter(author=user)     # filter all Note objects by user
    
    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save(author=self.request.user)
        else:
            print(serializer.errors)

# This class Destroy the Note because is child of DestroyAPIView
class NoteDelete(generics.DestroyAPIView):
    serializer_class = NoteSerializer
    permission_classess = [IsAuthenticated]

    # Show all notes of the authenticated user
    def get_queryset(self):
        user = self.request.user    # ask which is the user
        return Note.objects.filter(author=user)     # filter all Note objects by user