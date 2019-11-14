from django.shortcuts import render
from rest_framework import status, generics, permissions
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rede.paginations import *

from rede.models import Profile, Post, Comment
from rede.permissions import *
from rest_framework.throttling import ScopedRateThrottle
from rede.serializer import *

class ProfileList(generics.ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileListSerializer
    name = 'profile-list'
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    
    def perform_create(self, serializer):
       serializer.save(owner=self.request.user)

class ProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileDetailSerializer
    name = 'profile-detail'
    permission_classes = (IsOwnerOrReadOnly,)

#################################################################################################################

class CommentList(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentListSerializer
    name = 'comment-list'
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        #id_post = self.request.POST.get("pk")
        a = self.request.user
        b = a.usuarios.get()
        #c = Post.objects.filter(id = 1)
        serializer.save(email=b)
       # serializer.save(postId = c)

class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentListSerializer
    name = 'comment-detail'
    permission_classes = (IsOwnerOrReadOnly3,)

#################################################################################################################

class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostListSerializer
    name = 'post-list'
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        a = self.request.user
        b = a.usuarios.get()
        serializer.save(userId=b)

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostListSerializer
    name = 'post-detail'
    permission_classes = (IsOwnerOrReadOnly2,)

    

#################################################################################################################

class ProfilePostList(generics.ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfilePostSerializer
    pagination_class = ProfilePostPagination
    name = 'profile-post'
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class PostCommentList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostCommentSerializer
    pagination_class = PostCommentPagination
    name = 'post-comment'
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

#################################################################################################################

class ApiRootProfile(generics.GenericAPIView):
    name = 'root-proflie'

    def get(self, request,*args,**kwargs):
        return Response({
        'profiles': reverse(ProfileList.name,request=request),
        'posts': reverse(PostList.name,request=request),
        'comments': reverse(CommentList.name,request=request),
        'profile-posts': reverse(ProfilePostList.name, request=request),
        'posts-comments': reverse(PostCommentList.name,request=request),
})