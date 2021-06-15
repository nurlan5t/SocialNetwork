from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    phone = models.CharField(max_length=20)
    last_activity = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.username
