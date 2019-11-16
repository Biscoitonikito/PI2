"""
Book: Building RESTful Python Web Services
Chapter 2: Working with class based views and hyperlinked APIs in Django
Author: Gaston C. Hillar - Twitter.com/gastonhillar
Publisher: Packt Publishing Ltd. - http://www.packtpub.com
"""
from django.urls import path
from rede import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('profiles/', views.ProfileList.as_view(), name= views.ProfileList.name),
    path('profiles/<int:pk>/', views.ProfileDetail.as_view(), name=views.ProfileDetail.name),
    path('posts/', views.PostList.as_view(), name=views.PostList.name),
    path('posts/<int:pk>/', views.PostDetail.as_view(), name=views.PostDetail.name),
    path('comments/', views.CommentList.as_view(), name=views.CommentList.name),
    path('comments/<int:pk>/', views.CommentDetail.as_view(), name=views.CommentDetail.name),
    
    path('profile-posts/', views.ProfilePostList.as_view(), name=views.ProfilePostList.name),
    path('profile-comments/', views.PostCommentList.as_view(),name= views.PostCommentList.name),

    path('api-token-auth/', obtain_auth_token),
    path('', views.ApiRootProfile.as_view(), name= views.ApiRootProfile.name),
]