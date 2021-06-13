from django.shortcuts import render,redirect
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.template.context_processors import csrf
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages
from django.core.mail import send_mail

def login(request):
    c = {} 
    c.update(csrf(request)) 
    return render(request,'login.html', None)

def signup(request):
    return render(request,'signup.html', None)

def forgotpass(request):
    c = {} 
    c.update(csrf(request)) 
    return render(request,'Login_App/password_reset/done/')

def validate(request):
    username=request.POST.get('username','')
    if len(username) < 5 :
        msg="USERNAME MUST BE OF ATLEAST 5 CHARACTERS"
        return render(request,'signup.html',{'msg':msg})
    password=request.POST.get('password','')
    repassword=request.POST.get('repassword','')
    if password==repassword :
        if len(password) < 6 :
            msg="PASSWORD MUST BE OF ATLEAST 6 CHARACTERS"
            return render(request,'signup.html',{'msg':msg})
        email=request.POST.get('email','')
        #address=request.POST.get('address','')
        try :
            details=User.objects.create_user(username=username,password=password,email=email)
            details.save()
        except :
            msg="USER WITH THIS NAME ALREADY EXISTS"
            return render(request,'signup.html',{'msg':msg})
        user=auth.authenticate(username=username,password=password)
        auth.login(request,user)
        return HttpResponseRedirect('/Home/home/')
    else :
        msg="PASSWORDS DOESN'T MATCH"
        return render(request,'signup.html',{'msg':msg})

def authentication(request):     
    username = request.POST.get('username', '') 
    password = request.POST.get('password', '')
    user=auth.authenticate(username=username,password=password)
    if user is not None :
        auth.login(request,user)
        return HttpResponseRedirect('/Home/home/')
    else: 
        msg="Invalid Username/Password"
        return render(request,'login.html',{'msg':msg})

def logout(request) :
    auth.logout(request)
    return redirect('/Login_App/login/')

def adminlogin(request) :
    return render(request,'adminlogin.html',None)

def admincheck(request) :
    username = request.POST.get('username', '') 
    password = request.POST.get('password', '')
    user=auth.authenticate(username=username,password=password)
    if username=='user10702' and password=='user10702' :
        auth.login(request,user)
        return HttpResponseRedirect('/Add_Art/addart/')
    else :
        msg="Invalid Username/Password"
        return render(request,'adminlogin.html',{'msg':msg})