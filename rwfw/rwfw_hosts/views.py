from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hostmanager(request):
    # print(mhost)
    return HttpResponse("Host Manager Da")


def hostadd(request):
    return HttpResponse("Add Host")
