from django.db import models


class rwfw_host_type(models.Model):
    type_img  = models.ImageField(upload_to='images/')
    type_name = models.CharField(max_length=20, default='VMware')

    def __str__(self):
        return self.type_name



# Create your models here.
class rwfw_host_table(models.Model):
    host_name =models.CharField(max_length=50, default='lavans')
    host_ip   = models.GenericIPAddressField()
    host_user = models.CharField(max_length=20, default='root')
    host_pass = models.CharField(max_length=20, default='pass')
    host_type = models.IntegerField(default=1)
    # host_type = models.CharField(choices=[ (o.id, o.type_name) for o in rwfw_host_types.objects.all()])


    def __str__(self):
        return self.host_name
