from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Note

#Serializer converts the json data into python code and vize versa
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields =  ["id", "username", "password"]
        extra_kwargs = {"password": {"write_only": True}}
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data) #Dictionary split up and sent as json
        return user
    
class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ["id", "title", "content", "created_at", "author"]
        extra_kwargs = {"author": {"read_only": True}} #Can't be set by user, just by backend.