from django.contrib.auth.models import AbstractBaseUser, AbstractUser
from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from person.models import User


# Create your models here.
class Car(models.Model):
    name = models.CharField(max_length=200)
    code = models.IntegerField(unique=True)
    color = models.CharField(max_length=200)
    plaque = models.CharField(max_length=200)
    user = models.ForeignKey(User, related_name='Car', on_delete=models.CASCADE, null=True)

    def get_full_name(self):
        return self.name
