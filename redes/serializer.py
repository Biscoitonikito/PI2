from rest_framework import serializers

from redes.models import Profile, Post, Comment

class ProfileSerializer(serializers.HyperlinkedModelSerializer):  
    class Meta:
        model = Profile
        fields = ('pk', 'name', 'email', 'address')

class PostSerializer(serializers.HyperlinkedModelSerializer):
    userId = serializers.SlugRelatedField(queryset=Profile.objects.all(), slug_field='id')
    
    class Meta:
        model = Post
        fields = ('pk','title', 'body', 'userId')

class CommentSerializer(serializers.HyperlinkedModelSerializer):
    postId = serializers.SlugRelatedField(queryset=Post.objects.all(), slug_field='id')
    email = serializers.SlugRelatedField(queryset=Post.objects.all(), slug_field='email')


    class Meta:
        model = Comment
        fields = ('pk', 'name', 'email', 'body', 'postId')