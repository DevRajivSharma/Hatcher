from django.urls import path
from .views import *
app_name = 'dashboard'
urlpatterns = [
    path('', home, name='home'),
    path('profile',profile,name='profile'),
    path('job_search/', job_search, name='job_search'),
    path('job_search_ajax/',job_search_ajax,name='job_search_ajax'),
    path('job_detail/<int:job_id>/', job_detail, name='job_detail'),
    path('apply_job/<int:job_id>/', apply_job, name='apply_job'),
    path('applications', applications, name='applications'),
    path('load-jobs/', load_jobs, name='load_jobs'),
]
