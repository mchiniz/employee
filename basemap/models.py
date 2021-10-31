from django.contrib.auth.models import AbstractBaseUser, AbstractUser
from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from person.models import User

from django.db import models


class BaseMap(models.Model):
    name = models.CharField(max_length=200)
    url = models.URLField(max_length=200)
    user = models.ManyToManyField(User,  related_name='basemap', null=True)

    def get_full_name(self):
        return self.name
