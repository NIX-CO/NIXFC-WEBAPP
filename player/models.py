from django.db import models
from django.contrib.auth.models import User

class Player(User):
    bio = models.TextField(blank=True, null=True)
    photo = models.ImageField(upload_to='player_photos/',default='images/user.png')  # Field for player photo
    weight = models.FloatField()  # Field for player weight
    height = models.FloatField()  # Field for player height
    position = models.CharField(max_length=100,default="")  # Field for player position
    phone = models.CharField(max_length=20,default="")  # Field for player phone

