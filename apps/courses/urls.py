from django.urls import path
from .views import CourseAPIView

urlpatterns = [
    path('courses/', CourseAPIView.as_view(), name='course-list'),  # GET request to list all courses, POST request to create a new course
    path('courses/<int:id>/', CourseAPIView.as_view(), name='course-detail'),  # GET request for a single course, PUT/PATCH to update, DELETE to delete
]