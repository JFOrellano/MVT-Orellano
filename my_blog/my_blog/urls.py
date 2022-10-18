"""my_blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from course.views import create_course
from django.contrib import admin
from django.urls import include, path
from family.views import create_family
from profesor.views import create_profesor
from student.views import create_student

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("home.urls")),
    path("create_course/<str:name>/<int:code>", create_course),
    path(
        "create_profesor/<str:name>/<str:last_name>/<str:email>/<str:profession>",
        create_profesor,
    ),
    path("create_student/<str:name>/<str:last_name>/<str:email>", create_student),
    path("course/", include("course.urls")),
    path("student/", include("student.urls")),
    path("create_family/<str:name>/<str:last_name>/<str:email>/<str:birth_date>", create_family),
    path("family/", include("family.urls")),
]
