from django.contrib import admin
from .models import *
# Register your models here.
class JobAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'company__name', 'job_type','created_at', 'updated_at')
    search_fields = ['id', 'title', 'company__name', 'job_type','created_at', 'updated_at']
    list_filter = ['created_at', 'updated_at']

admin.site.register(employer_table)
admin.site.register(company)
admin.site.register(Job, JobAdmin)
admin.site.register(req_skill)