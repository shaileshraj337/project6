from urllib import response
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hi(request):
    return HttpResponse('hi, whats going on')
