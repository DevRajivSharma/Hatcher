from django.contrib import admin
from django.urls import path,include
from .views import *
import dashboard.urls
app_name = 'employer'
urlpatterns = [
    path('',employer_login,name='employer_login'),
    path('employer_register',employer_register,name='employer_register'),
    path('employer_dashboard',employer_dashboard,name='employer_dashboard'),
    path('employer_logout',employer_logout,name='employer_logout'),
    path('add_job',add_job,name='add_job'),
    path('company_register',company_register,name='company_register'),
    path('user_profile/<int:id>/', user_profile, name='user_profile'),
    path('search_candidate/', search_candidate, name='search_candidate'),
    path('applications', applications, name='applications'),
    path('posted_jobs', posted_jobs, name='posted_jobs'),
    path('applicants_user/<int:job_id>', applicants_user, name='applicants_user'),
    path('edit_company/<int:cmp_id>', edit_company, name='edit_company'),
    path('delete_company/<int:cmp_id>', delete_company, name='delete_company'),
    path('accept_applicant/<int:job_id>/<int:user_id>', accept_applicant, name='accept_applicant'),
    path('reject_applicant/<int:job_id>/<int:user_id>', reject_applicant, name='reject_applicant'),
    # path('employer_dashboard/', include('employer_dashboard.urls', namespace='employer_dashboard')), 
]
