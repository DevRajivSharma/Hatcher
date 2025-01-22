from django.urls import path
from .views import *
app_name = 'complete_profile'
urlpatterns = [
    path('',basic_detail,name='basic_detail'),
    path('resume/',resume,name='resume'),
    path('skip',skip,name='skip'),
]