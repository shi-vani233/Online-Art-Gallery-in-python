from django.shortcuts import render,redirect
from django.views.generic import TemplateView 
from django.http import HttpResponseRedirect
from django.contrib import messages
from Add_Art.models import art
from django.contrib.auth.models import User
from .models import view_cart

def home(request) :
    if not request.user.is_authenticated :
        return redirect('/Login_App/login/')
    else :
        username=request.user.username
        if username=='user10702' :
            return redirect('/Add_Art/addart/')
        arts=art.objects.filter(available=1)[0:3]
        return render(request,'home.html',{'arts':arts})

def profile(request):
    if not request.user.is_authenticated :
        return redirect('/Login_App/login/')
    else :
        username=request.user.username
        if username=='user10702' :
            return redirect('/Add_Art/addart/')
        args={'user':request.user}
        return render(request,'profile.html',args)


def search(request) :
    if not request.user.is_authenticated :
        return redirect('/Login_App/login/')
    category=request.GET.get('category','')
    results=art.objects.filter(category=category,available=1)
    username=request.user.username
    if username=='user10702' :
        return redirect('/Add_Art/addart/')
    if results.exists() :
        arts=results
        return render(request,'search.html',{'arts':arts})   #write code to show results
    else :
        arts=art.objects.filter(available=1)[0:3]
        msg="no product available of your search.sorry:("
        return render(request,'home.html',{'msg':msg,'arts':arts})

def purchases_view(request) :
    if not request.user.is_authenticated :
        return redirect('/Login_App/login/')
    username=request.user.username
    if username=='user10702' :
        return redirect('/Add_Art/addart/')
    arts=art.objects.filter(username=username,available=0)
    if arts.exists() :
        return render(request,'purchases_view.html', {'arts':arts})  #write code to show results
    else :
        msg="you have not purchased anything yet."
        return render(request,'purchases_view.html',{'msg':msg})
        

def cart_view(request) :
    if not request.user.is_authenticated :
        return redirect('/Login_App/login/')
    username=request.user.username
    if username=='user10702' :
        return redirect('/Add_Art/addart/')    
    results=view_cart.objects.filter(username=username)
    if results.exists() :
        arts=[]
        for result in results :
            name=result.artname
            obj=art.objects.get(artname=name)
            arts.append(obj)
        return render(request,'cart_view.html', {'arts':arts})  #write code to show results
    else :
        msg="your cart is empty. add your favorites here."
        return render(request,'cart_view.html',{'msg':msg})


def new_purchase(request) :
    if not request.user.is_authenticated :
        return redirect('/Login_App/login/')
    username=request.user.username
    if username=='user10702' :
        return redirect('/Add_Art/addart/')    
    getartname=request.POST.get('img','')
    artname=art.objects.get(artname=getartname)
    artname.available=0
    artname.username=request.user.username
    artname.save()
    username=request.user
    obj=view_cart.objects.filter(username=username,artname=getartname)
    obj.delete()
    arts=art.objects.filter(artname=getartname)
    return render(request,'new_purchase.html',{'arts':arts})

def cart(request) :
    if not request.user.is_authenticated :
        return redirect('/Login_App/login/')
    getartname=request.POST.get('img','')
    artname=art.objects.get(artname=getartname)
    artname.username=request.user.username
    artname.save()
    results=view_cart.objects.filter(artname=getartname,username=request.user)
    if results.exists():
        arts=art.objects.all()
        msg="This item is already in your cart."
        return render(request,'home.html',{'msg':msg,'arts':arts})
    else:
        log=view_cart(artname=getartname,username=request.user)
        log.save()
        arts=art.objects.all()
        msg="successfully added to your cart"
        return render(request,'home.html',{'arts':arts,'msg':msg})

def remove(request):
    if not request.user.is_authenticated :
        return redirect('/Login_App/login/')
    art_name=request.POST.get('img','')
    username=request.user
    obj=view_cart.objects.filter(username=username,artname=art_name)
    obj.delete()
    results=view_cart.objects.filter(username=username)
    if results.exists() :
        arts=[]
        for result in results :
            name=result.artname
            obj=art.objects.get(artname=name)
            arts.append(obj)
        msg="succesfully deleted from cart"    
        return render(request,'cart_view.html', {'arts':arts,'msg':msg})  #write code to show results
    else :
        msg="your cart is empty."
        return render(request,'cart_view.html',{'msg':msg})