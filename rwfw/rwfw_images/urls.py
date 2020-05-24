from django.urls import re_path, path
from .import views



urlpatterns = [
    # re_path(r'/Host Manager', views.hostmanager,name="hostmanager"),
    # path('<int:item_id>', views.activities,name="rwfwops"),
    path('ListImage/<typename>', views.imagelist, name="imagelist"),
    re_path(r'^Image', views.imagemanager, name="imagemanager"),
]
