from django.shortcuts import render
from django.http import HttpResponse
from .models import rwfw_image_downloaded
from .models import rwfw_image_type
from .models import rwfw_image_repo

# Create your views here.
def imagemanager(request):
    db1_obj = rwfw_image_type.objects.all()
    return render(request,'images.html',{'items':db1_obj})


def imagelist(request,typename):
    print(typename)
    context = {'tpname':typename}
    db1_obj = rwfw_image_type.objects.filter(type_name=typename)
    # db2_obj = rwfw_image_repo.objects.none();
    db3_obj = rwfw_image_downloaded.objects.none();
    try:
        # print(db1_obj[0].id)
        # print(db1_obj[0].type_name)
        # db2_obj = rwfw_image_repo.objects.filter(repo_type=db1_obj[0].id)
        context['tpurl']=db1_obj[0].type_img
        db3_obj = rwfw_image_downloaded.objects.filter(dwn_type=db1_obj[0].id)
    except:
        # print("Query Error")
        context['tpurl'] = ''
    # context['imagetable'] = db2_obj
    context['downtable'] = db3_obj
    return render(request,'listimage.html',context)
