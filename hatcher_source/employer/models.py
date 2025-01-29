from django.db import models
from django.db.models.signals import *
from django.core.validators import RegexValidator
from django.utils.timesince import timesince
from django.utils.timezone import is_aware, make_aware, get_current_timezone
from datetime import datetime
class employer_table(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_no = models.CharField(
        max_length=10, 
        unique=True, 
        validators=[RegexValidator(r'^\d{10}$', 'Phone number must be a 10-digit number.')],
        null=True
    )
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)  # Store hashed passwords
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    age = models.CharField(max_length=10, null=True)
    updated_at = models.DateTimeField(auto_now=True)
    company_exist = models.BooleanField(default=False)
    def __str__(self):
        return self.email
    
class company(models.Model):
    recruiter = models.ForeignKey(employer_table,on_delete=models.CASCADE,related_name='company',null=True)
    cmp_email = models.EmailField(null=True)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    city = models.CharField(max_length=200)
    total_staff = models.IntegerField(default=1)
    image = models.ImageField(upload_to='company_images', null=True,
                              default='company_images/default.png')
    created_at = models.DateTimeField(auto_now_add=True,null=True)
    def __str__(self) :
        return self.name

class Job(models.Model):
    WORK_TYPE_CHOICES = [
        ('Work from home', 'Work from home'),
        ('Work from office', 'Work from office'),
        ('Field Job', 'Field Job')
    ]
    JOB_TYPE_CHOICES = [
        ('Full time', 'Full time'),
        ('Part time', 'Part time'),
        ('Internship', 'Internship'),
        ('Hourly', 'Hourly')
    ]
    EXPERIENCE_CHOICES = [
        ('Fresher','Fresher'),
        ('1 year', '1 year'),
        ('1-3 years', '1-3 years'),
        ('3-6 years', '3-6 years'),
        ('6-10 years', '6-10 years'),
        ('10+ years', '10+ years'),
    ]
    company = models.ForeignKey(company, on_delete=models.CASCADE, related_name='job')
    title = models.CharField(max_length=100)
    job_type = models.CharField(max_length=100, null=True, choices=JOB_TYPE_CHOICES)
    work_type = models.CharField(max_length=100, null=True, choices=WORK_TYPE_CHOICES)
    description = models.TextField()
    location = models.CharField(max_length=100)
    salary_disclose = models.BooleanField(default=True)
    salary_minimum = models.IntegerField( blank=True, null=True)
    salary_maximum = models.IntegerField( blank=True, null=True)
    total_vacancy = models.IntegerField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    experience = models.CharField(max_length=100,null=True,choices=EXPERIENCE_CHOICES)
    perks = models.CharField(max_length=100,null=True)
    current_application = models.IntegerField(default=0,null=True)
    def __str__(self):
        return self.title 
    @property
    def timesince(self):
        """
        Dynamically calculates and returns the time passed since 'updated_at'
        in a human-readable format.
        """
        now = datetime.now()
        if is_aware(self.updated_at):
            now = make_aware(now, get_current_timezone())
        time_diff = timesince(self.updated_at, now)
        return f"{time_diff.split(', ')[0]} ago"  # Return the first time unit (e.g., '2 days ago')


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