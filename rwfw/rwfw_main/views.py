from django.shortcuts import render
from django.http import HttpResponse
from .models import rwfw_item_table

# Create your views here.
def index(request):
    #return HttpResponse("RWFW Initial.")
    db1_obj = rwfw_item_table.objects.all()
    return render(request,'index.html', {'items':db1_obj})
