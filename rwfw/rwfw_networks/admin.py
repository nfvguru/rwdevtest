from django.contrib import admin
from .models import rwfw_nw_type
from .models import rwfw_nw_system
from .models import rwfw_nw_vlan

# Register your models here.
admin.site.register(rwfw_nw_type)
admin.site.register(rwfw_nw_system)
admin.site.register(rwfw_nw_vlan)
