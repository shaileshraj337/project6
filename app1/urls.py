from nturl2path import url2pathname
from app1.views import hi
from django.urls import path
app_name='app1'
urlpatterns=[
    path('hi/', hi, name='hi'),
]