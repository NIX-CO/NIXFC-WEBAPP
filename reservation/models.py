from django.db import models
from django.forms import ValidationError
from Fields.models import Field

class Reservation(models.Model):
    
    field = models.ForeignKey(Field, on_delete=models.CASCADE,null=True,blank=True)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    

    def __str__(self):
        return f"{self.field} réservé par {self.user}"
    
    def clean(self):
        # Check for conflicts with existing reservations
        conflicts = Reservation.objects.filter(field=self.field, end_time__gte=self.start_time, start_time__lte=self.end_time)
        if conflicts.exists():
            raise ValidationError("Le terrain est déjà réservé pour cette période.")