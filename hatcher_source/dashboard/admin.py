from django.contrib import admin
from .models import *

# Custom admin for Like model

# Custom admin for Job model


# Custom admin for Application model
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'job', 'application_date', 'status')
    search_fields = ['user__email', 'job__title']
    list_filter = ['application_date', 'status']


admin.site.register(Application, ApplicationAdmin)

