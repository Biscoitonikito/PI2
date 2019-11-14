from django.db import models

# Create your models here.

class Profile(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    address = models.CharField(max_length=150)
    
    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

class Post(models.Model):

    title = models.CharField(max_length=100)
    body = models.TextField()
    userId = models.ForeignKey(Profile, related_name = "profile", on_delete=models.CASCADE)

    class Meta:
        ordering = ('-id',)

    def __str__(self):
        return self.body


class Comment(models.Model):

    name = models.CharField(max_length=100)
    email = models.ForeignKey(Profile, related_name = "author", on_delete=models.CASCADE)
    body = models.TextField()
    postId = models.ForeignKey(Post, related_name = "post", on_delete=models.CASCADE)

    class Meta:
        ordering = ('-id',)
    def __str__(self):
        return self.body
