from django.urls import path
from .views import home, j_search

app_name = 'dashboard'
urlpatterns = [
    path('', home, name='home'),
    path('job_search', j_search, name='j_search'),
]
