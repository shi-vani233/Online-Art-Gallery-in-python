from django.http import HttpResponse 
from django.shortcuts import render, redirect 
from .models import art
from django.template.context_processors import csrf 
from django.contrib import auth

def addart(request):
    if not request.user.is_authenticated :
        return redirect('/Login_App/login/')
    a={}
    a.update(csrf(request))
    username=request.user.username
    if username=='user10702' :
        return render(request,'addart.html',a)
    else :
        return redirect('/Home/home/')

def add(request):   
    artname=request.POST.get('artname','')
    category=request.POST.get('category','')
    prize=request.POST.get('prize','')
    username=request.user.username
    if(request.FILES.get('image','')):
        image=request.FILES['image']
        if(artname is None or category is None or prize is None or image is None) :
            msg="Fill All The Fields"
            return render(request,'addart.html',{'msg':msg})
        log=art(artname=artname,category=category,prize=prize,image=image,username=username,available=1)
        log.save()
        msg="Successfully Uploaded."
        return render(request,'addart.html',{'msg':msg})
    else:
        render(request,'addart.html')
        msg="fill all the details"
        return render(request,'addart.html',{'msg':msg})
   
def logout(request) :
    auth.logout(request)
    return redirect('/Login_App/login/')

def viewall(request):
    if not request.user.is_authenticated :
        return redirect('/Login_App/login/')
    arts=art.objects.all()
    username=request.user.username
    if username=='user10702' :
        return render(request,'viewart.html',{'arts':arts})
    else :
        return redirect('/Home/home/')

def delete_art(request):
    if not request.user.is_authenticated :
        return redirect('/Login_App/login/')
    art_name=request.POST.get('img','')
    a=art.objects.get(artname=art_name)
    a.delete()
    a=art.objects.all()
    msg="deleted successfully"
    return render(request,'viewart.html',{'arts':a,'msg':msg})


