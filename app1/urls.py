from app1.views import *
from django.urls import path
app_name='happy'

urlpatterns=[
    path('project11/',project11,name='project11'),
    path('first/',first,name='first'),
]