from django.urls import path
from .views import *
app_name = 'complete_profile'
urlpatterns = [
    path('',basic_detail,name='basic_detail'),
    path('resume/',resume,name='resume'),
    path('skip',skip,name='skip'),
    path('edit_job_preference',edit_job_preference,name='edit_job_preference'),
    path('delete-resume/<int:resume_id>/', delete_resume, name='delete_resume'),
    path('update_profile_image', update_profile_image, name='update_profile_image'),
]