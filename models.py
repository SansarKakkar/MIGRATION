from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    full_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'email'  # Use email as the username field
    REQUIRED_FIELDS = ['username', 'full_name']  # Additional required fields

    def __str__(self):
        return self.email
