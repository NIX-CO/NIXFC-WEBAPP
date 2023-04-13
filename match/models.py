from django.db import models

class Match(models.Model):
    teamhome = models.CharField(max_length=100)
    teamaway = models.CharField(max_length=100)
    scorehome = models.IntegerField(null=True, blank=True)
    scoreaway = models.IntegerField(null=True, blank=True)
    date = models.DateTimeField()
    status = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.teamhome} vs {self.teamaway}"