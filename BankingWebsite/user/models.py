from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    balance = models.IntegerField(default=0)
    PhoneNumber = models.TextField(max_length=10,null=True)