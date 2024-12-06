from django.db import models
from credentials.models import *
# Create your models here.
from employer.models import *

    
class Application(models.Model):
    user = models.ForeignKey(user_table, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    application_date = models.DateField()
    status = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.user.email} - {self.job.title}"
class Internship(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    company_name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    stipend = models.CharField(max_length=50, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
class Skill(models.Model):
    skill_name = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.skill_name


