from rest_framework import serializers

from rede.models import Profile, Post, Comment
from django.contrib.auth.models import User

class ProfileListSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Profile
        fields = ('pk', 'name', 'email','address', 'url')

class ProfileDetailSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Profile
        fields = ('pk', 'owner','name', 'email', 'address')

##################################################################################################################

class CommentListSerializer(serializers.HyperlinkedModelSerializer):
    postId = serializers.SlugRelatedField(queryset=Post.objects.all(), slug_field='id')
    #email = serializers.SlugRelatedField(queryset=Profile.objects.all(), slug_field='id')
    class Meta:
        model = Comment
        fields = ('pk', 'name', 'body', 'postId', 'url')

class PostComment(serializers.HyperlinkedModelSerializer):
     class Meta:
         model = Comment
         fields = ('name', 'email', 'body', 'url')


##################################################################################################################

class PostListSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = ('pk', 'title', 'body', 'url')

class ProfilePost(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = ('title', 'body', 'url', 'userId')

##################################################################################################################

class ProfilePostSerializer(serializers.HyperlinkedModelSerializer):
    posts = ProfilePost(many=True, read_only=True)
    class Meta:
        model = Profile
        fields = ('pk', 'name', 'email', 'url', 'posts')

class PostCommentSerializer(serializers.HyperlinkedModelSerializer):
    comment = PostComment(many=True, read_only=True)
    class Meta:
        model = Post
        fields = ('pk', 'title', 'body', 'userId', 'comment', 'url')

##################################################################################################################