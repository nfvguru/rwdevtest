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
    return HttpResponse("List Images")
# Create your views here.
