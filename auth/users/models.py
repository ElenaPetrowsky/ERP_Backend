from pyexpat import model
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    username = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=30)
    email = models.EmailField()
    password = models.CharField(max_length=100)

    
    REQUIRED_FIELDS = []