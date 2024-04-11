from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics
from .serializers import UserSerializer, NoteSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Note

# Create your views here.
class NoteListCreate(generics.ListCreateAPIView): #Lists because it has multiple requests possible
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self): #Override from Django docs
        user = self.request.user
        return Note.objects.filter(author=user)
    
    def perform_create(self, serializer): #Another Override, more like an extension
        if serializer.is_valid():
            serializer.save(author=self.request.user) ##Legger på enda ett felt
        else: 
            print(serializer.errors)

class NoteDelete(generics.DestroyAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self): #Override from Django docs
        user = self.request.user
        return Note.objects.filter(author=user)



class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]
