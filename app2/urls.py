from app2.views import *
from django.urls import path
app_name='hello'


urlpatterns=[
    path('project/',project,name='project'),
    path('second/',second,name='second'),
]