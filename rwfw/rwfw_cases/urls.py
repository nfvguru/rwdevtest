from django.urls import re_path, path
from .import views



urlpatterns = [
    re_path(r'^Case', views.casemanager, name="casemanager"),
]
