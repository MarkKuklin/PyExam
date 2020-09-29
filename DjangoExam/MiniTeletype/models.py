from django.db import models

# Create your models here.
class User(models.Model):
    user_name = models.CharField(max_length=50)
    email = models.EmailField()
    avatar = models.ImageField()

# class Post(models.Model):
#     header = models.CharField(max_length=256)

