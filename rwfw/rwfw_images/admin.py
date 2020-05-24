from django.contrib import admin
from .models import rwfw_image_downloaded
from .models import rwfw_image_type
from .models import rwfw_image_repo
# Register your models here.
admin.site.register(rwfw_image_repo)
admin.site.register(rwfw_image_type)
admin.site.register(rwfw_image_downloaded)
# Register your models here.
