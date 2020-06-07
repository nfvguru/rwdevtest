from django.db import models

# Create your models here.
# Create your models here.

class rwfw_nw_vlan(models.Model):
    vlan_name = models.CharField(max_length=20, default='default')
    vlan_vlan = models.CharField(max_length=20, default='default')
    vlan_label = models.CharField(max_length=40, default='default')
    vlan_host_id = models.IntegerField(default=1)

    def __str__(self):
        return self.vlan_name


class rwfw_nw_system(models.Model):
    nw_name = models.CharField(max_length=20, default='test')
    nw_ip = models.GenericIPAddressField()
    nw_hostname = models.CharField(max_length=100, default='localhost')
    nw_port   = models.IntegerField(default=22)
    nw_user  = models.CharField(max_length=20, default='test')
    nw_pass  = models.CharField(max_length=20, default='test')
    nw_type = models.IntegerField(default=1)
    nw_mgmt_vlan = models.CharField(max_length=20, default=None)
    nw_data1_vlan = models.CharField(max_length=20, default=None)
    nw_data2_vlan = models.CharField(max_length=20, default=None)
    nw_host_id = models.IntegerField(default=1)

    def __str__(self):
        return self.nw_name

class rwfw_nw_type(models.Model):
    type_img  = models.ImageField(upload_to='images/')
    type_name = models.CharField(max_length=20, default='ova')

    def __str__(self):
        return self.type_name
