from course import views
from django.urls import path

app_name = "course"
urlpatterns = [
    path("courses", views.courses, name="course-list"),
]
