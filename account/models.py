from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from .manager import MyUserManager
from django.utils import timezone


# Create your models here.
class User(AbstractBaseUser):
    email = models.EmailField(unique=True)
    last_online = models.DateTimeField(default=timezone.now)
    username=models.CharField(max_length=125,null=True,blank=True)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ""
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_special_user = models.BooleanField(default=False)
    password_expire = models.DateTimeField(default=timezone.now)
    is_demand=models.BooleanField(default=False)
    # last_activity=models.DateTimeField(blank=True,null=True)
    objects = MyUserManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin
