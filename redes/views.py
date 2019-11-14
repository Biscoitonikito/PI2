from django.shortcuts import render
from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.reverse import reverse

from redes.models import Profile, Post, Comment
from redes.serializer import ProfileSerializer, PostSerializer, CommentSerializer

class ProfileList(generics.ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    name = 'profile-list'

class ProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    name = 'profile-detail'
# Create your views here.

