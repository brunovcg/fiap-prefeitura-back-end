from django.db import models
from django.contrib.auth.models import AbstractUser

class User (AbstractUser):

  name = models.CharField(max_length=255, null=False)
  telefone = models.CharField(max_length=15, null=False)
  persona = models.IntegerField(null=False)