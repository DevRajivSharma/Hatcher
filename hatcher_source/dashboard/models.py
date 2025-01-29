from django.db import models
from credentials.models import *
# Create your models here.
from employer.models import *

    
class Application(models.Model):
    STATUS_CHOICES = (
        ('Pending', 'Pending'),
        ('Accepted', 'Accepted'),
        ('Rejected', 'Rejected'),
    )
    user = models.ForeignKey(user_table, on_delete=models.CASCADE, related_name='applications')
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name='applications')
    application_date = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    status = models.CharField(max_length=100, choices=STATUS_CHOICES, default='Pending')

    def __str__(self):
        return f"{self.user.email} - {self.job.title}"



