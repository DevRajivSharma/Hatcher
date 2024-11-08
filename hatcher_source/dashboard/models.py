from django.db import models

# Create your models here.
class user_table(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_no = models.CharField(max_length=10,unique=True)
    user_bio = models.CharField(max_length=500)
    user_profile_image = models.ImageField(upload_to='user_profile_image', blank=True, null=True)
    email =  models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    username = 'email'
    def __str__(self):
        return self.email