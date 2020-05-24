import os
import subprocess as sp
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
    public_cloud = 0
    context = {'tpname':typename}
    if typename == 'Azure':
        public_cloud = 1
    elif typename == 'AWS':
        public_cloud = 2
    db1_obj = rwfw_host_type.objects.filter(type_name=typename)
    db2_obj = rwfw_host_table.objects.none();
    try:
        # print(db1_obj[0].id)
        # print(db1_obj[0].type_name)
        db2_obj = rwfw_host_table.objects.filter(host_type=db1_obj[0].id)
        context['tpurl']=db1_obj[0].type_img
    except:
        # print("Query Error")
        context['tpurl'] = ''
    context['hosttable'] = db2_obj
    context['reachable'] = 0
    host_ip = ""
    if public_cloud == 1:
        host_ip = 'portal.azure.com'
        context['host_ip'] = host_ip
        context['reachable'] = 1
    elif public_cloud == 2:
        host_ip = 'console.aws.amazon.com'
        context['host_ip'] = host_ip
        context['reachable'] = 1
    elif db2_obj.exists():
        host_ip = db2_obj[0].host_ip
        # print(db2_obj[0].host_name)
        print(os.name)
        ping_opt = '-c 1 '
        if os.name == 'nt':
            ping_opt = '-n 1 '
        command = 'ping ' + ping_opt + host_ip
        # print(command)
        # Can even be 'python manage.py somecommand'
        child = sp.Popen(command, shell=True,stdout=sp.PIPE)
        streamdata = child.communicate()[0]
        rc = child.returncode
        if rc == 0:
            context['reachable'] = 1
    return render(request,'listhost.html',context)
