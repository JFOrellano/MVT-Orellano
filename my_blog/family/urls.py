from django.urls import path
from family import views

app_name = "family"
urlpatterns = [
    path("family_list", views.family_list, name="family-list"),
]
