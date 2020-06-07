from django.shortcuts import render
from django.http import HttpResponse
from .models import rwfw_nw_type
from .models import rwfw_nw_system
from .models import rwfw_nw_vlan

# Create your views here.
# Create your views here.
def nwmanager(request):
    db1_obj = rwfw_nw_type.objects.all()
    return render(request,'networks.html',{'items':db1_obj})



def nwlist(request,typename):
    # print(typename)
    context = {'tpname':typename}
    db1_obj = rwfw_nw_type.objects.filter(type_name=typename).first()
    db2_obj = rwfw_nw_system.objects.none();
    nwid = 0
    try:
        nwid = db1_obj.id
        # print(nwid)
        context['nwid'] = nwid
        context['tpurl']=db1_obj.type_img
        # print(context)
        if typename == 'VLAN':
            context['vlan']=1
            db2_obj = rwfw_nw_vlan.objects.all()
        else:
            context['vlan']=0
            db2_obj = rwfw_nw_system.objects.filter(nw_type=nwid)
            # print(context)
    except:
        print ('error')
        context['tpurl'] = ''

    context['items'] = db2_obj
    # print(context)
    return render(request,'listnetwork.html',context)
