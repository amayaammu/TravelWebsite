from django.shortcuts import render,redirect
from django.http import HttpResponse
from traveladmin. models import *
from . models import *
# Create your views here.
def index2(request):
    data = traveldb.objects.all()
    return render(request,'index2.html',{'data':data})

def contact(request):
    return render(request,'contact.html')


def about(request):
    return render(request,'about.html')

def register(request):
    return render(request,'register.html')

def userlogin(request):
    return render(request,'userlogin.html')

def getweb(request):
    if request.method=="POST":
        name=request.POST.get('name')
        phone=request.POST.get('phone')
        message=request.POST.get('message')
        data=contactdb(name=name,phone=phone,message=message)
        data.save()
    return redirect('index2')

def regi(request):
    if request.method=="POST":
        name=request.POST.get('name')
        phone=request.POST.get('phone')
        uname=request.POST.get('uname')
        password=request.POST.get('password')
        data=registerdb(name=name,phone=phone,uname=uname,password=password)
        data.save()
    return redirect('index2')
def userin(request):
    uname = request.POST.get('username')
    password = request.POST.get('password')
    if registerdb.objects.filter(uname=uname,password=password).exists():
        data = registerdb.objects.filter(uname=uname,password=password).values('name','phone','id').first()
        request.session['name'] =data['name']
        request.session['phone'] = data['phone']
        request.session['uname'] = uname
        request.session['password'] = password
        request.session['id'] = data['id']
        return redirect('index2')
    else:
        return redirect('userlogin')

def logout(request):
    del request.session['name']
    del request.session['phone']
    del request.session['uname']
    del request.session['password']
    del request.session['id']
    return redirect('index2')

def registerations(request):
    data=registerdb.objects.all()
    return render(request,'registerations.html',{'data':data})