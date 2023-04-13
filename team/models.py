from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Team(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField()
    logo = models.ImageField(upload_to='team_logos/')
    number_of_members = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(20)])
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)

    def __str__(self):
        return self.name