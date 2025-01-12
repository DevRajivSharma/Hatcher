from django.urls import path
from .views import *

app_name = 'dashboard'
urlpatterns = [
    path('', home, name='home'),
    path('job_search/', job_search, name='job_search'),
    path('job_detail/<int:job_id>/', job_detail, name='job_detail'),
]
