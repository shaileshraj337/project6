from app2.views import hello
from django.urls import path
app_name='app2'
urlpatterns=[
    path('hello/', hello, name='hello'),
]