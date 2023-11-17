from django.contrib import admin
from django.urls import path
from nz.views import *
app_name='kohili'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('virat/',virat,name='virat'),
]