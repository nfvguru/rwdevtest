from django.urls import re_path, path
from .import views



urlpatterns = [
    re_path(r'^Deployment', views.dpmanager, name="dpmanager"),
]
