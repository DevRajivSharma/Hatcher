from django.urls import path
from .views import *

app_name = 'community_post'  # Make sure this line is included
urlpatterns = [ 
    path('post_list',post_list, name='post_list'),
    path('add_post',add_post,name='add_post'),
    path('toggle_like/<int:post_id>/',toggle_like,name='toggle_like'),
    path('post_filter',post_filter,name='post_filter'),
    path('my_post',my_post,name='my_post'),
    path('delete_post/', delete_post, name='delete_post'),

]
