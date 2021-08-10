from django.shortcuts import render
from . models import *
# Create your views here.

def index(request):
    plc=place.objects.all()
    new=news.objects.all()
    return render(request,'index.html',{'plc':plc,'new':new})
