
from django.contrib import admin

from django.urls import path, include

from api.views import student_api
from home.views import *
from vege.views import *

urlpatterns = [
    path('studentapi/', student_api, name="student_api"),
]
