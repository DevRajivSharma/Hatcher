from django.urls import path
from .views import *

app_name = 'community_post'  # Make sure this line is included
urlpatterns = [ 
    path('', post_list, name='post_list')
]
