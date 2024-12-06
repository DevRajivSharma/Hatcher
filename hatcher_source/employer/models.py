from django.db import models
from django.db.models.signals import *
from django.dispatch import receiver
# Create your models here.
class employer_table(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_no = models.CharField(max_length=10,unique=True)
    email =  models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    username = models.EmailField(unique=True,default=None)
    created_at = models.DateTimeField(auto_now_add=True,null=True)
    age = models.CharField(max_length=10,null=True)
    updated_at = models.DateTimeField(auto_now=True)
    company_exist = models.BooleanField(default=False)
    def save(self, *args, **kwargs):
        self.username = self.email
        super().save(*args, **kwargs)
    def __str__(self):
        return self.email
    
class company(models.Model):
    recruiter = models.ForeignKey(employer_table,on_delete=models.CASCADE,related_name='company',null=True)
    hr = models.EmailField(null=True)
    name = models.CharField(max_length=100)
    bio = models.CharField(max_length=1000)
    address = models.CharField(max_length=200)
    employees = models.IntegerField(default=1)
    image = models.ImageField(upload_to='company_images', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True,null=True)
    def __str__(self) :
        return self.name
class Job(models.Model):
    company = models.ForeignKey(company,on_delete=models.CASCADE,related_name='job')
    title = models.CharField(max_length=100)
    description = models.TextField()
    location = models.CharField(max_length=100)
    salary = models.CharField(max_length=50, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title 
class req_skill(models.Model):
    job = models.ForeignKey(Job,on_delete=models.CASCADE,related_name='req_skill')
    imp_skill = models.CharField(max_length=100)
    skill_2 = models.CharField(max_length=50)
    skill_3 = models.CharField(max_length=50)
    skill_4 = models.CharField(max_length=50)
    education = models.CharField(max_length=100)
    speak_lng_1 = models.CharField(max_length=50)
    speak_lng_2 = models.CharField(max_length=50)
    def __str__(self) :
        return self.imp_skill