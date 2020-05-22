from django.contrib import admin
from .models import rwfw_host_type
from .models import rwfw_host_table
# Register your models here.
admin.site.register(rwfw_host_type)
admin.site.register(rwfw_host_table)
