from django.contrib import admin
from django.urls import path, include
from course.views import *

urlpatterns = [
    path('courses/', CourseListView.as_view()),
    path('courses/<int:pk>', CourseDetailView.as_view()),
]