from django.db import models
# Create your models here.
class user_table(models.Model):
    first_name = models.CharField(max_length=100,null=True)
    last_name = models.CharField(max_length=100,null=True)
    # phone_no = models.CharField(max_length=10,unique=True,null=True)
    # user_bio = models.CharField(max_length=500,null=True)
    user_profile_image = models.ImageField(upload_to='user_profile_image', blank=True, 
                                           default='logos/default_user.png')
    email =  models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    username = models.EmailField(unique=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True,null=True)
    # age = models.CharField(max_length=10,null=True)
    updated_at = models.DateTimeField(auto_now=True)
    complete_profile = models.BooleanField(default=False)
    def save(self, *args, **kwargs):
        self.username = self.email
        super().save(*args, **kwargs)
    def __str__(self):
        return self.email



class FeedBack(models.Model):
    name = models.CharField(max_length=100, default='Anonymous')
    email = models.EmailField(max_length=100)
    feedback = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name + ' - ' + self.email