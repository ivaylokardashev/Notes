from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import generics
from .serializers import UserSerializer


class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all() # Check if there is similiar user
    serializer_class = UserSerializer # What data to be accept
    permission_classes = [AllowAny] # Give permission to all
