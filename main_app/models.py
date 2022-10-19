from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Account(models.Model):
    # extension of default user table
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    # phone number used for verification
    email = models.CharField(max_length=40, null=True)
    credit_grade = models.CharField(max_length=4, default="FFF")
    country = models.CharField(max_length=57, null=True)
    state = models.CharField(max_length=57, null=True)
    birthdate = models.DateField(null=True)
    system_username = models.CharField(max_length=30, unique=True, null=True)
    net_worth = models.DecimalField(max_digits=20, decimal_places=2, default=0) 

class UserAssets(models.Model):
    id_asset = models.AutoField(primary_key=True)
    email = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    type = models.CharField(max_length=20, null=True)
    name = models.CharField(max_length=255, null=True)
    worth = models.DecimalField(max_digits=20, decimal_places=2, default=0)
    extra_field = models.CharField(max_length=57, null=True)

