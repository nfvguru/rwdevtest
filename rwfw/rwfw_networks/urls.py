from django.urls import re_path, path
from .import views



urlpatterns = [
    path('ListNetwork/<typename>', views.nwlist, name="nwlist"),
    re_path(r'^Network', views.nwmanager, name="nwmanager"),
]
