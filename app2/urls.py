from django.urls import path
from app2.views import *
app_name='login'
urlpatterns=[
    path('login/',login,name='login')
]