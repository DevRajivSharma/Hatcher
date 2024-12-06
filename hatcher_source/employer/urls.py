from django.contrib import admin
from django.urls import path,include
from .views import *
import dashboard.urls
urlpatterns = [
    path('',employer_login,name='employer_login'),
    path('employer_register',employer_register,name='employer_register'),
    path('employer_dashboard',employer_dashboard,name='employer_dashboard'),
    path('employer_logout',employer_logout,name='employer_logout'),
    path('start_hiring',start_hiring,name='start_hiring'),
    path('company_register',company_register,name='company_register')
    # path('employer_dashboard/', include('employer_dashboard.urls', namespace='employer_dashboard')), 
]
