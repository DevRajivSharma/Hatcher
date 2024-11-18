from django.contrib import admin
from .models import user_table, Post, Like, Job, Application, Internship, Skill, Comment

# Custom admin for user_table model
class UserTableAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'email', 'phone_no', 'user_bio', 'age', 'created_at', 'updated_at')
    search_fields = ['email', 'first_name', 'last_name']
    list_filter = ['created_at', 'updated_at']

# Custom admin for Post model
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'content', 'created_at')
    search_fields = ['content']
    list_filter = ['created_at']

# Custom admin for Like model

# Custom admin for Job model
class JobAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'company_name', 'location', 'salary', 'created_at', 'updated_at')
    search_fields = ['title', 'company_name']
    list_filter = ['created_at', 'updated_at']

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

# Custom admin for Comment model
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'post', 'user', 'content', 'created_at')
    search_fields = ['post__id', 'user__email']
    list_filter = ['created_at']

# Register models with their respective custom admin classes
admin.site.register(user_table, UserTableAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Like)
admin.site.register(Job, JobAdmin)
admin.site.register(Application, ApplicationAdmin)
admin.site.register(Internship, InternshipAdmin)
admin.site.register(Skill, SkillAdmin)
admin.site.register(Comment, CommentAdmin)
