from django.contrib import admin
from django.urls import path,include
from .views import *
import dashboard.urls

urlpatterns = [
    path('',landing_page,name='landing_page'),
    path('employer_login/',include('employer.urls')),
    path('login/',login,name='login'),
    path('register/',register,name='register'),
    path('logout/',logout,name='logout'),
    path('dashboard/', include('dashboard.urls', namespace='dashboard')), 
]
