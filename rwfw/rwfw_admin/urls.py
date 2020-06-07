"""rwfw_admin URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', include('rwfw_main.urls')),
    path('', include('rwfw_hosts.urls')),
    path('', include('rwfw_images.urls')),
    path('', include('rwfw_dploymnts.urls')),
    path('', include('rwfw_flavors.urls')),
    path('', include('rwfw_networks.urls')),
    path('', include('rwfw_results.urls')),
    path('', include('rwfw_steps.urls')),
    path('', include('rwfw_tests.urls')),
    path('', include('rwfw_cases.urls')),
    path('supermanager/', admin.site.urls),
]

urlpatterns +=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
urlpatterns +=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
