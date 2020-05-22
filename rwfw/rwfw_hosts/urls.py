from django.urls import re_path
from .import views



urlpatterns = [
    # re_path(r'/Host Manager', views.hostmanager,name="hostmanager"),
    # path('<int:item_id>', views.activities,name="rwfwops"),
    re_path(r'^HostAdd', views.hostadd, name="hostadd"),
    re_path(r'^Host', views.hostmanager, name="hostmanager"),
]
