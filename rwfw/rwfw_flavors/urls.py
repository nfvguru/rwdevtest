from django.urls import re_path, path
from .import views



urlpatterns = [
    re_path(r'^Flavor', views.flavormanager, name="flavormanager"),
]