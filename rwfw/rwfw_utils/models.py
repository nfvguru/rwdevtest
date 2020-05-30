import os
from django.conf import settings
from django.db import models


def jsons_path():
    return os.path.join(settings.BASE_DIR,'rwfw_local/json')


class rwfw_utils_imgdownload(models.Model):
    imgdwn_path = models.CharField(max_length=200, default='/projects')
    imgdwn_name = models.CharField(max_length=20, default='dwnScript')
    json_path = models.FilePathField(path=jsons_path,match="*.json", recursive=True)

    def __str__(self):
        return self.imgdwn_name
