from django.urls import path
from .import views



urlpatterns = [
    path('', views.index,name="index"),
    path('<int:item_id>', views.activities,name="rwfwops"),
    path('<mtype>', views.handlemanagers,name="mtype"),
]
