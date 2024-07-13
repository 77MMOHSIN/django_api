from django.db import models

# Create your models here.
class User(models.Model):
    name=models.CharField(max_length=12)
    email=models.CharField(max_length=23)
    password=models.CharField(max_length=8)
