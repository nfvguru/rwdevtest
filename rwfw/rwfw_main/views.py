from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import rwfw_item_table

# Create your views here.
def index(request):
    #return HttpResponse("RWFW Initial.")
    db1_obj = rwfw_item_table.objects.all()
    for titem in db1_obj:
       print(titem.item_icon.url)

    return render(request,'index.html',{'items':db1_obj})

def activities(request, item_id):
    #print(item_id)
    item_link=get_object_or_404(rwfw_item_table, pk=item_id)
    return render(request, 'items.html', {'item_link':item_link})
