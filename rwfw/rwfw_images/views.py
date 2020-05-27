from django.shortcuts import render
from django.http import HttpResponse
from .models import rwfw_image_downloaded
from .models import rwfw_image_type
from .models import rwfw_image_repo
from .tasks import adding_task
from .tasks import rwfw_download_image
from django.views import View

# Create your views here.
def imagemanager(request):
    db1_obj = rwfw_image_type.objects.all()
    return render(request,'images.html',{'items':db1_obj})


def imagelist(request,typename):
    print(typename)
    context = {'tpname':typename}
    db1_obj = rwfw_image_type.objects.filter(type_name=typename).first()
    db2_obj = rwfw_image_repo.objects.none();
    db3_obj = rwfw_image_downloaded.objects.none();
    repoid = 0
    try:
        repoid = db1_obj.id
        context['repoid'] = repoid
        context['tpurl']=db1_obj.type_img
        db3_obj = rwfw_image_downloaded.objects.filter(dwn_type=repoid)
    except:
        context['tpurl'] = ''

    try:
        db2_obj = rwfw_image_repo.objects.filter(repo_type=repoid)
    except:
        print("No repo objects")

    # context['imagetable'] = db2_obj
    context['downtable'] = db3_obj
    context['vertable'] = db2_obj

    # task = adding_task.delay(9,4)
    # context['task_id'] = task.id
    # context['task_status'] = task.status
    # if task.status == 'SUCCESS':
    #     context['task_results'] = task.get()

    return render(request,'listimage.html',context)

class DownloadTaskView(View):
    def get(self, request, task_id, task_version, task_build):
        print(task_id)
        print(task_version)
        print(task_build)
        db1_obj = rwfw_image_repo.objects.filter(repo_type=task_id, repo_verson=task_version, repo_build=task_build).first()
        if db1_obj:
            print("Download image from")
            print(db1_obj.repo_ip)
            print("at path")
            dip   = db1_obj.repo_ip
            duser = db1_obj.repo_user
            dpass = db1_obj.repo_pass
            dpath = db1_obj.repo_base
            dpath += db1_obj.repo_verson + "/"
            my_build = db1_obj.repo_build
            if my_build == '0':
                my_build="lastSuccessfulBuild"
            dpath += my_build +"/HW_CH_ODS-VA/DEBUG/"
            if task_id == 1:
                my_type = 'VMW'
            elif task_id == 2:
                my_type = 'ISO'
            elif task_id == 3:
                my_type = 'img'
            elif task_id == 4:
                my_type = 'KVM'
            dpath += my_type
            print(dpath)
            task = rwfw_download_image.delay(dip, duser, dpass, dpath)
        return HttpResponse('Vandithangayya')
        # return JsonResponse(response_data)
