from django.db import models
from django.contrib.auth.models import User
class Image(models.Model):
    photo = models.ImageField(upload_to="myimage")
    date = models.DateTimeField(auto_now_add=True)
    
class Profile(models.Model):
    user = models.OneToOneField(User,null=True,on_delete = models.CASCADE)
    foto = models.ImageField(default='default.jpg' ,upload_to="profile_foto")
    bio = models.CharField(max_length = 100)