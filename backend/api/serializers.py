# Creating new users 
# API accept JSON object for creating new user
# API create DJANGO USER object and return it
# serializers get data from frontend which are JSON and add it to database
from django.contrib.auth.models import User
from .models import Note
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User # Represents the user in Django
        fields = ["id", "username", "password"] # The fields we want to serialize
        extra_kwargs = {"password": {"write_only": True}} # Signal to don't show return password

    def create(self, validate_data):
        user = User.objects.create_user(**validate_data) # Function which unpack fields and create user
        return user
    
class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ["id", "title", "content", "created_at", "author"]
        extra_kwargs = {"author": {"read_only": True}}

