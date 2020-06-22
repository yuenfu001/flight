from django.db import models

# Create your models here.
class Flight(models.Model):
    origin = models.CharField(max_length = 100)
    destination = models.CharField(max_length = 100)
    duration = models.IntegerField()

    def _str_(self):
        return f"{self.id} - {self.origin} to {self.destination}"
