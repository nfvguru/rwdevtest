from django.urls import re_path, path
from .import views



urlpatterns = [
    # re_path(r'/Host Manager', views.hostmanager,name="hostmanager"),
    # path('<int:item_id>', views.activities,name="rwfwops"),
    path('ListHost/<typename>', views.hostlist, name="hostlist"),
    re_path(r'^Host', views.hostmanager, name="hostmanager"),
]
