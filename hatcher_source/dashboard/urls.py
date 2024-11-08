from django.contrib import admin
from django.urls import path, include
from .views import *
import community_post.urls
app_name = 'dashboard' 
urlpatterns = [
    path('', home, name='home'),
    path('community_post/', include('community_post.urls', namespace='community_post')),
]
