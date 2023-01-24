from django.shortcuts import render, HttpResponse
from .models import *

def Studentinfo(request):
    # return HttpResponse("<h1>View1.1</h1>")
    fname = request.POST.get("fname")
    lname = request.POST.get("lname")
    age = int(request.POST.get("age"))
    gender = int(request.POST.get("gender"))
    
    if gender==1:
        gender=True
    elif gender==2:
        gender=False
    else:
        gender=None

    print(fname,lname,age,gender)

    Student.objects.create(fname=fname,
                           lname=lname, 
                            age=age,
                            gender=gender)


    return HttpResponse("-__-__-___-")

def view1(request):
    return render(request,"home/view1.html",context={})