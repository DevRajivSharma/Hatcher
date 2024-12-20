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
    username = models.EmailField(unique=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True,null=True)
    age = models.CharField(max_length=10,null=True)
    updated_at = models.DateTimeField(auto_now=True)
    def save(self, *args, **kwargs):
        self.username = self.email
        super().save(*args, **kwargs)
    def __str__(self):
        return self.email
