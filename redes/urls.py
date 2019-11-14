"""
Book: Building RESTful Python Web Services
Chapter 2: Working with class based views and hyperlinked APIs in Django
Author: Gaston C. Hillar - Twitter.com/gastonhillar
Publisher: Packt Publishing Ltd. - http://www.packtpub.com
"""
from django.urls import path
from redes import views

urlpatterns = [
    path('profiles/', views.ProfileList.as_view(), name= views.ProfileList.name),
    path('profiles/<int:pk>/', views.ProfileDetail.as_view, name=views.ProfileDetail.name),
    
    #path('profile-posts/'),
    #path('profile-posts/<int:pk>/'),
    
    '''
    path('posts-cooments/'),
    path('posts-cooments/<int:pk>'),
    path('posts/<int:pk>/comments'),
    path('posts/<int:pk>/comments/<int:pk2>'),
    path('resumo/'),
    '''
]