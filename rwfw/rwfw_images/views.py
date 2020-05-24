from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def imagemanager(request):
    # print(mhost)
    # db1_obj = rwfw_host_type.objects.all()
    # return render(request,'hosts.html',{'items':db1_obj})
    return HttpResponse("Image Manager Da")


def imagelist(request,typename):
    return HttpResponse("List Images")
# Create your views here.
