from dhoni.views import *
from django.urls import path
app_name='nothing'
urlpatterns=[
    path('csk/',csk,name='csk'),
]