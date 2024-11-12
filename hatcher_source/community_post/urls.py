from django.urls import path
from .views import *

app_name = 'community_post'  # Make sure this line is included
urlpatterns = [ 
    path('post_pist',post_list, name='post_list'),
    path('add_post',add_post,name='add_post')
]
