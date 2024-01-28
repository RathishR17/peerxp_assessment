
from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)

class UserProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='user_profile')
    role = models.CharField(max_length=50, choices=[('Admin', 'Admin'), ('Member', 'Member')])

class Expense(models.Model):
    name = models.CharField(max_length=140)
    date = models.DateField()
    category = models.CharField(max_length=50, choices=[('Health', 'Health'), ('Electronics', 'Electronics'), ('Travel', 'Travel'), ('Education', 'Education'), ('Books', 'Books'), ('Others', 'Others')])
    description = models.TextField()
    amount = models.PositiveIntegerField()
    created_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
