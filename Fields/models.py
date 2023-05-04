from django.db import models
from organization.models import Organization

# Create your models here.

class Field(models.Model):
    SIZE_CHOICES = (
        ('5', 'Size 5'),
        ('7', 'Size 7'),
        ('11', 'Size 11')
    )

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    size = models.CharField(max_length=2, choices=SIZE_CHOICES)
    image = models.ImageField(upload_to='field_images/')
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)

    def __str__(self):
        return self.name