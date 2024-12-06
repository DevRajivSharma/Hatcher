from django.contrib import admin
from .models import *

# Custom admin for Like model

# Custom admin for Job model


# Custom admin for Application model
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'job', 'application_date', 'status')
    search_fields = ['user__email', 'job__title']
    list_filter = ['application_date', 'status']

# Custom admin for Internship model
class InternshipAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'company_name', 'location', 'stipend', 'created_at', 'updated_at')
    search_fields = ['title', 'company_name']
    list_filter = ['created_at', 'updated_at']

# Custom admin for Skill model
class SkillAdmin(admin.ModelAdmin):
    list_display = ('id', 'skill_name', 'description')
    search_fields = ['skill_name']
    list_filter = ['skill_name']




# Register models with their respective custom admin classes


admin.site.register(Application, ApplicationAdmin)
admin.site.register(Internship, InternshipAdmin)
admin.site.register(Skill, SkillAdmin)

