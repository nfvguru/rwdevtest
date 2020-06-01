from django.shortcuts import render
from django.http import HttpResponse
from .models import rwfw_image_downloaded
from .models import rwfw_image_type
from .models import rwfw_image_repo
from .tasks import adding_task
from .tasks import rwfw_chkdownload_image
from .tasks import rwfw_dodownload_image
from django.views import View
from django.http import JsonResponse
from celery import current_app
from rwfw_local.utils.rwfw_download_utils import build_path_from_db

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
        db1_obj = rwfw_image_repo.objects.filter(repo_type=task_id, repo_verson=task_version, repo_build=task_build).first()
        if db1_obj:
            dip   = db1_obj.repo_ip
            duser = db1_obj.repo_user
            dpass = db1_obj.repo_pass
            dpath = build_path_from_db(db1_obj, task_id)
            # print(dpath)
            task = rwfw_chkdownload_image.delay(dip, duser, dpass, dpath)
            response_data = {
                't_id': task.id,
                't_status': task.status,
            }
            # return HttpResponse(json.dumps(response_data), content_type='application/json')
            return JsonResponse(response_data)
        return HttpResponse('Vandithangayya')
        # return JsonResponse(response_data)

class DoDownloadTaskView(View):
    def get(self, request, task_id, task_version, task_build):
        db1_obj = rwfw_image_repo.objects.filter(repo_type=task_id, repo_verson=task_version, repo_build=task_build).first()
        if db1_obj:
            dip   = db1_obj.repo_ip
            duser = db1_obj.repo_user
            dpass = db1_obj.repo_pass
            dpath = build_path_from_db(db1_obj, task_id)
            print (dpath)
            task = rwfw_dodownload_image.delay(dip, duser, dpass, dpath)
            response_data = {
                't_id': task.id,
                't_status': task.status,
            }
            return JsonResponse(response_data)
        return HttpResponse('Download Not Possible')

class DownloadTaskMonitor(View):
    def get(self, request, task_id):
        task = current_app.AsyncResult(task_id)
        response_data = {'task_status': task.status, 'task_id': task.id}
        if task.status == 'SUCCESS':
            response_data['task_build'] = task.get()
        return JsonResponse(response_data)
