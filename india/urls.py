from django.contrib import admin
from django.urls import path
from india.views import *
app_name='rohit'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('msd/',msd,name='msd'),
]