from django.db import models

# Create your models here.
class Flight(models.Model):
    origin = models.Charfield(max_lenght=100)
    destination = models.Charfield(max_lenght=100)
    duration = models.Integer()
