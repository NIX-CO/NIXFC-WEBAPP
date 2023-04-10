from django.db import models
from django.contrib.auth.models import User
from Fields.models import Field

class Room(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    users_list = models.ManyToManyField(User, related_name='rooms')
    field = models.ForeignKey(Field, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"Room {self.id} {self.users_list}"

