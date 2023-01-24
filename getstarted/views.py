# from contextlib import _RedirectStream
from pyexpat.errors import messages
from django.shortcuts import render, HttpResponse,redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login,logout
# Create your views here.
def playzone(request):
    return render(request,"getstarted/playzone.html")

def signup_request(request):
    if request.method== "POST":
        username=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('cpassword2')
        
        print(pass1, pass2)

        try:
            User.objects.get(email=email)
            
            return HttpResponse('Email Already exists')
        except:
            pass

        try:
            User.objects.get(username=username)
            
            return HttpResponse('username Already exists')
        except:
            pass
        
        if not pass1==pass2:
            return HttpResponse('Enter different password')

        email.lower()
        myuser=User.objects.create_user(username,email)
        print(myuser)
        myuser.set_password(pass1)
        myuser.save()

        return redirect('signin')

    return render(request,"getstarted/signup.html")

def signin_request(request):
    if request.method == 'POST':
        email=request.POST.get('email')
        password1=request.POST.get('password1')
        
        # print(email, password1)

        try:
            uname = User.objects.get(email=email).username
            
            user=authenticate(request,username=uname,password=password1)
            # print(user)
        except:
            return HttpResponse(request,'Email not in records')
        
        # print(user)

        if user == None: 
            return HttpResponse("No User exists")    
        
        login(request,user)
        return redirect('signin')
        
    else:
        return render(request,"getstarted/signin.html")

def signout_request(request):
    logout(request)
    return redirect('playzone')

def tictac(request):
    
    statuss=request.GET.get("wl")
    winningIndex=request.GET.get("board")
    IndexX=request.GET.get("countX")
    IndexO=request.GET.get("countO")
    print(request.GET)
    
    print(statuss,winningIndex,IndexX,IndexO)
    
    Tictac.objects.create(statuss=statuss,
                          winningIndex=winningIndex,
                          IndexX=IndexX,
                          IndexO=IndexO)
    
    return render(request, "getstarted/playzone.html", context={})