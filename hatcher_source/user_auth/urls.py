from django.urls import path,include
from .views import *
urlpatterns = [
    path('',email_auth,name='email_auth'),
    path('verify-otp/',verify_otp)
]

