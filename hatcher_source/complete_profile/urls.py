from django.urls import path
from .views import *
appname = 'complete_profile'
urlpatterns = [
    path('basic_detail/',basic_detail,name='basic_detail'),
    path('education/',education,name='education'),
    path('experience/',experience,name='experience'),
    path('language/',language,name='language'),
    path('resume/',resume,name='resume'),
]