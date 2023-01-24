# from http.client import HTTPResponse
from django.shortcuts import render,HttpResponse
from .models import *
# from Projects.studentportal.tryMediaFiles.models import MediaFiles

# Create your views here.
def mediaFiles(request):

    if request.method == 'POST':

        print(request.FILES.get('file'))
        curr_user= MediaFiles.objects.create(fname=request.POST.get('fname'),
                                              email=request.POST.get('email'),)
        print(curr_user)
        curr_user.photo=request.FILES.get('file')
        curr_user.save()
        return  HttpResponse("From Filled Successfully")

    else:
        return render(request,'tryMediaFiles/mediaFiles.html',context={})