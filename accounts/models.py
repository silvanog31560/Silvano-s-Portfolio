from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    username = models.CharField(max_length=150, blank=True, unique=True)
    email = models.EmailField('Email Address', max_length=254, unique=True)

    def __str__(self):
        return self.username
