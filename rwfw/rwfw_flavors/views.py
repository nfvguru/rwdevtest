from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

# Create your views here.
# Create your views here.
def flavormanager(request):
    # db1_obj = rwfw_image_type.objects.all()
    # return render(request,'images.html',{'items':db1_obj})
    return HttpResponse('Flavor manager DA')
