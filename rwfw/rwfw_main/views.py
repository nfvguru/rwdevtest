from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import rwfw_item_table

# Create your views here.
def index(request):
    #return HttpResponse("RWFW Initial.")
    db1_obj = rwfw_item_table.objects.all()
    visit_count = request.session.get('num_visit',0) + 1
    request.session['num_visit'] = visit_count
    return render(request,'index.html',{'items':db1_obj,'visit_count':visit_count})

def activities(request, item_id):
    #print(item_id)
    act_item = get_object_or_404(rwfw_item_table,pk=item_id)
    return render(request, 'myitems.html', {'selops':act_item})
