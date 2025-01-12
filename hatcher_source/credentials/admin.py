from django.contrib import admin
# Custom admin for user_table model
from .models import *
class UserTableAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'email', 'phone_no',  'created_at', 'updated_at')
    search_fields = ['email', 'first_name', 'last_name']
    list_filter = ['created_at', 'updated_at']


admin.site.register(user_table, UserTableAdmin)
admin.site.register(FeedBack)
