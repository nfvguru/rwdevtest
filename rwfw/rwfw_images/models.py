from django.db import models

# Create your models here.

class rwfw_image_repo(models.Model):
    repo_ip = models.GenericIPAddressField()
    repo_name = models.CharField(max_length=20, default='default')
    repo_user = models.CharField(max_length=20, default='root')
    repo_pass = models.CharField(max_length=20, default='root')
    repo_base = models.CharField(max_length=50, default='/projects')
    repo_verson = models.CharField(max_length=20, default='1.1')
    repo_build = models.CharField(max_length=20, default='0')

    def __str__(self):
        return self.repo_name

class rwfw_image_downloaded(models.Model):
    dwn_version = models.CharField(max_length=20, default='1.1')
    dwm_build = models.CharField(max_length=20, default='100')
    dwn_index = models.IntegerField(default=0)
    dwn_path = models.CharField(max_length=50, default='Builds/')
    dwm_avail = models.IntegerField(default=1)

    def __str__(self):
        return self.dwn_version + '_' + self.dwn_build

class rwfw_image_type(models.Model):
    type_img  = models.ImageField(upload_to='images/')
    type_name = models.CharField(max_length=20, default='ova')
    type_count = models.IntegerField(default=2)

    def __str__(self):
        return self.type_name
