from django.contrib import admin
from .models import *

# Custom admin for Post model
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'content', 'total_likes','created_at')
    search_fields = ['content']
    list_filter = ['created_at']
# Custom admin for Like model
class LikAdmin(admin.ModelAdmin):
    list_display = ('post__id', 'user__email', 'post__content','created_at')
    search_fields = ['post__content','user__email']
    list_filter = ['post__content','user__id',]
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'post', 'user', 'content', 'created_at')
    search_fields = ['post__id', 'user__email']
    list_filter = ['created_at']
# Register your models here.
admin.site.register(Post, PostAdmin)
admin.site.register(Like,LikAdmin)
admin.site.register(Comment, CommentAdmin)