from django.contrib import admin

from .models import *

admin.site.register(user_table)
admin.site.register(Job)
admin.site.register(Application)
admin.site.register(Internship)
admin.site.register(Skill)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Like)