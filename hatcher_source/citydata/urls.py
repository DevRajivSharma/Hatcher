from django.contrib import admin
from django.urls import path,include
from .views import *
urlpatterns = [
    path('',search_city,name='search_city'),
]