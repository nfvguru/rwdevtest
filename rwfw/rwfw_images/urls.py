from django.urls import re_path, path
from .import views



urlpatterns = [
    # re_path(r'/Host Manager', views.hostmanager,name="hostmanager"),
    # path('<int:item_id>', views.activities,name="rwfwops"),
    path('ListImage/<typename>', views.imagelist, name="imagelist"),
    path('Download/<int:task_id>/<str:task_version>/<str:task_build>', views.DownloadTaskView.as_view(), name="download"),
    path('StatusDownload/<str:task_id>/', views.DownloadTaskMonitor.as_view(), name='taskmonitor'),
    re_path(r'^Image', views.imagemanager, name="imagemanager"),
]
