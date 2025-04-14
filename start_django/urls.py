from django.contrib import admin
from django.urls import path

from first_project.views import Home_page, current_time, workdir, recipe, create_phone, get_phone

urlpatterns = [
    path('', Home_page),
    path('current_time/', current_time),
    path('workdir/', workdir),
    path('recipe/<str:str_>', recipe),
    path('create_phone/', create_phone),
    path('catalog/', get_phone),

]
