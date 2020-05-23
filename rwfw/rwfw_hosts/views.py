import os
import subprocess
from django.shortcuts import render
from django.http import HttpResponse
from .models import rwfw_host_type
from .models import rwfw_host_table

# Create your views here.
def hostmanager(request):
    # print(mhost)
    db1_obj = rwfw_host_type.objects.all()
    return render(request,'hosts.html',{'items':db1_obj})
    # return HttpResponse("Host Manager Da")


def hostlist(request,typename):
    # print(typename)
    db1_obj = rwfw_host_type.objects.filter(type_name=typename)
    db2_obj = rwfw_host_table.objects.filter(host_type=db1_obj[0].id)
    # print(db2_obj[0].host_name)
    command = 'ping -n 1 ' + db2_obj[0].host_ip
     # Can even be 'python manage.py somecommand'
    child = subprocess.Popen(command, shell=True)
    # returncode = child.poll()
    print(child.returncode)
    # return HttpResponse("Host List")
    return render(request,'listhost.html',{'tpname':typename,'tpurl':db1_obj[0].type_img, 'hosttable':db2_obj})
