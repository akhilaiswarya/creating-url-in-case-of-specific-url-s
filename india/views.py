from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def msd(request):
    return HttpResponse('<h1>Hiii this is msd template</h1>')
