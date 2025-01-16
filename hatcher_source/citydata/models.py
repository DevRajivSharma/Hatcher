from django.db import models

# Create your models here.
# models.py
from django.db import models

class CityState(models.Model):
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.city}, {self.state}"
