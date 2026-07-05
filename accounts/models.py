# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    mobile_number = models.CharField(max_length=15, unique=True)
    shop_name = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    address = models.TextField(blank=True, null=True)

    REQUIRED_FIELDS = ['mobile_number']