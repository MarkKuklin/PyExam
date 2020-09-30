from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField()

class Theme(models.Model):
    name = models.CharField(max_length=50)

class Post(models.Model):
    header = models.CharField(max_length=256)
    theme = models.ForeignKey(Theme, on_delete=models.PROTECT)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    pub_date = models.DateTimeField()
    text = models.CharField()


class Comment(models.Model):
    header = models.CharField(max_length=256)
    theme = models.ForeignKey(Theme, on_delete=models.PROTECT)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    pub_date = models.DateTimeField()
    text = models.CharField()