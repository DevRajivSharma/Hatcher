from django.db import models

# Create your models here.
class user_auth_otp(models.Model):
    mail = models.EmailField(unique=True)
    otp = models.IntegerField()