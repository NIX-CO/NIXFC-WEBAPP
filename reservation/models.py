from django.db import models
from Fields.models import Field

class Reservation(models.Model):
    
    field = models.ForeignKey(Field, on_delete=models.CASCADE,null=True,blank=True)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    def __str__(self):
        return f"{self.field} réservé par {self.user}"