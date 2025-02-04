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
    path('update_profile_name', update_profile_name, name='update_profile_name'),
    path('update_schooling_details', update_schooling_details, name='update_schooling_details'),
    path('update_language_details', update_language_details, name='update_language_details'),
    path('update_skills_details', update_skills_details, name='update_skills_details'),
    path('update_internship_details', update_internship_details, name='update_internship_details'),
    path('update_bio_details', update_bio_details, name='update_bio_details'),
    path('update_employment_details', update_employment_details, name='update_employment_details'),
]