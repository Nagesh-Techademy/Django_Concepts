
from django.urls import path, include
from viewset import views
from django.contrib import admin
from rest_framework.routers import DefaultRouter

router= DefaultRouter()
router.register('studentapimodelviewset', views.StudentModelViewSet, basename='StudentModelViewSet')

urlpatterns = [
    #path('studentapi/', student_api, name="student_api"),                              # Function Based view
    path('', include(router.urls)),            # Class Based view
]
