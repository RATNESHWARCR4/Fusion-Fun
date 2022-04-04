from distutils.command.upload import upload
from random import choices
from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid

from sympy import Max
# Create your models here.

AGE_Choice=(
    ('All','ALL'),
    ('Kids','Kids')
)
MOVIE_Choice=(
    ('Seasonal','Seasonal'),
    ('Single','Single')    
)

class CustomUser(AbstractUser):
    profiles=models.ManyToManyField('Profile',blank=True)
    
class Profile(models.Model):
    name=models.CharField(max_length=50)
    age_limit=models.CharField(max_length=10,choices=AGE_Choice)
    uuid=models.UUIDField(default=uuid.uuid4)
    
class Movie(models.Model):
    title=models.CharField(max_length=200)
    description=models.TextField(null=True,blank=True)
    created=models.DateTimeField(auto_now_add=True)
    uuid=models.UUIDField(default=uuid.uuid4)
    type=models.CharField(max_length=10,choices=MOVIE_Choice)
    videos=models.ManyToManyField('Video')
    flyer=models.ImageField(upload_to='flyers')
    age_limit=models.CharField(max_length=10,choices=AGE_Choice)
    
class Video(models.Model):    
    title=models.CharField(max_length=200,blank=True,null=True)
    file=models.FileField(upload_to='movies')
    

