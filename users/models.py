from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import CustomUserManager
from django.db import models


class User(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=50, blank=True, null=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    objects = CustomUserManager()
    USERNAME_FIELD = "email"
    EMAIL_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email
