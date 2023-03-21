from django.db import models

# Create your models here.
from django.db import models

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

    def __str__(self):
        return self.name
