from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class UserRoleOption(models.TextChoices):
    SUPER_ADMIN = "super_admin", "super_admin"
    ADMINISTRATION = "administration", "administration"
    BETTING_MANAGEMENT = "betting_management", "betting_management"
    TRANSACTION_MANAGEMENT = "transaction_management", "transaction_management"
    SETTINGS_MANAGEMENT = "settings_management", "settings_management"

class User(AbstractUser):
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=50, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    role = models.CharField(max_length=30, choices=UserRoleOption.choices)

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "1. User"

    def __str__(self):
        return self.username