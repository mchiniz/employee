from django.contrib.auth.models import AbstractBaseUser, AbstractUser
from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.db import models


class UserProfile(models.Model):
    biography = models.CharField(max_length=200)
    position = models.CharField(max_length=200)

    def get_biography(self):
        return self.biography


class User(AbstractUser):
    profile_user = models.OneToOneField(UserProfile, on_delete=models.CASCADE, null=True)

    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'
