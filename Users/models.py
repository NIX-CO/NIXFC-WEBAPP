from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=20)
    photo = models.ImageField(upload_to='photos/')
    address = models.CharField(max_length=100)

