from django.db import models
from credentials.models import user_table
from datetime import date,datetime
# Create your models here.
class UserDetail(models.Model):
    user = models.OneToOneField(user_table, on_delete=models.CASCADE, related_name='details')
    birth_date = models.DateField(null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    applying_for = models.CharField(max_length=255, null=True, blank=True)
    gender = models.CharField(max_length=10, null=True, blank=True)
    location = models.CharField(max_length=255, null=True, blank=True)
    student = models.BooleanField(default=False)
    education_level = models.CharField(max_length=255, null=True, blank=True)
    diploma_degree = models.CharField(max_length=255, null=True, blank=True)
    iti_degree = models.CharField(max_length=255, null=True, blank=True)
    graduate_degree = models.CharField(max_length=255, null=True, blank=True)
    postgraduate_degree = models.CharField(max_length=255, null=True, blank=True)
    specialization = models.CharField(max_length=255, null=True, blank=True)
    college_name = models.CharField(max_length=255, null=True, blank=True)
    college_start_date = models.DateField(null=True, blank=True)
    college_end_date = models.DateField(null=True, blank=True)
    school_medium = models.CharField(max_length=255, null=True, blank=True)
    work_experience = models.BooleanField(null=True, blank=True)
    job_title = models.CharField(max_length=255, null=True, blank=True)
    job_role = models.CharField(max_length=255, null=True, blank=True)
    company_name = models.CharField(max_length=255, null=True, blank=True)
    industry = models.CharField(max_length=255, null=True, blank=True)
    current_working = models.BooleanField(default=False)
    notice_period = models.CharField(max_length=255, null=True, blank=True)
    salary = models.IntegerField(null=True, blank=True)
    work_start_date = models.DateField(null=True, blank=True)
    work_end_date = models.DateField(null=True, blank=True)
    total_experience = models.IntegerField(null=True, blank=True)
    english_level = models.CharField(max_length=255, null=True, blank=True)
    other_languages = models.TextField(null=True, blank=True)  # You might want to save this as a comma-separated list
    day_shift = models.BooleanField(default=False)
    night_shift = models.BooleanField(default=False)
    work_from_home = models.BooleanField(default=False)
    work_from_office = models.BooleanField(default=False)
    field_job = models.BooleanField(default=False)
    full_time = models.BooleanField(default=False)
    part_time = models.BooleanField(default=False)
    hourly = models.BooleanField(default=False)
    skills = models.TextField(null=True,blank=True)
    def __str__(self):
        return f"Details of {self.user.email}"
    
    def save(self, *args, **kwargs):
        # Calculate age if birth_date is provided
        if self.birth_date:
            today = date.today()
            self.age = today.year - self.birth_date.year - ((today.month, today.day) < (self.birth_date.month, self.birth_date.day))
        else:
            self.age = None  # or you can leave it as is

        super().save(*args, **kwargs)  # Call the original save method
    @property
    def formatted_birth_date(self):
        if isinstance(self.birth_date, date):  # Use self to access the instance's birth_date
            day = self.birth_date.day
            suffix = 'th' if 11 <= day <= 13 else {1: 'st', 2: 'nd', 3: 'rd'}.get(day % 10, 'th')
            formatted_date = self.birth_date.strftime(f"{day}{suffix} %B %Y")
            return formatted_date
        return None

class userResume(models.Model):
    user = models.OneToOneField(user_table ,on_delete=models.CASCADE, related_name='resume')
    resume_file = models.FileField(upload_to='resume',null=True)
    created_at = models.DateTimeField(auto_now_add=True,null=True)  # Set once when the object is created
    updated_at = models.DateTimeField(auto_now=True,null=True) 
    def __str__(self):
        return f"{self.user}'s Resume"
    
class internship(models.Model):
    user = models.ForeignKey(user_table, on_delete=models.CASCADE, related_name='internships')
    company_name = models.CharField(max_length=255, null=True)
    job_title = models.CharField(max_length=255, null=True)
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)
    description = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)  # Set once when the object is created
    updated_at = models.DateTimeField(auto_now=True)  # Update every time the object is saved
    def __str__(self):
        return f"{self.user}'s Internship at {self.company_name}"