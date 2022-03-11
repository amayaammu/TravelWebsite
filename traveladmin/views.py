from django.shortcuts import render,redirect
from django.http import HttpResponse
from . models import *
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from webtravelapp.models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login


# Create your views here.
def index(request):
    tcount = traveldb.objects.all().count()
    scount = traveldb.objects.all().count()
    return render(request,'index.html',{'tcount':tcount,'scount':scount})

def add_destination(request):
    return render(request,'add_destination.html')

def view_destination(request):
    data = traveldb.objects.all()
    return render(request,'view_destination.html',{'data':data})

def getdata(request):
    if request.method=='POST':
        destination=request.POST.get('destination')
        location=request.POST.get('location')
        image=request.FILES['image']
        price=request.POST.get('price')
        data=traveldb(destination=destination,location=location,image=image,price=price)
        data.save()
    return redirect('view_destination')
    
def edit(request,trid):
    data = traveldb.objects.filter(id=trid)
    return render(request,'edit.html',{'data':data})
    
def update(request,uid):
    if request.method == 'POST':
       destination_c = request.POST.get('destination')
       location_c = request.POST.get('location')
       price_c = request.POST.get('price')
    traveldb.objects.filter(id=uid).update(destination=destination_c,location=location_c,price=price_c)
    try:
        image_r=request.FILES['image']
        fs = FileSystemStorage() 
        file = fs.save(image_r.name, image_r)
    except MultiValueDictKeyError :
        file=traveldb.objects.get(id=uid).image
    traveldb.objects.filter(id=uid).update(destination=destination_c,location=location_c,image=file,price=price_c)
    return redirect('view_destination')
def delete(request,did):
    traveldb.objects.get(id=did).delete()
    return redirect('view_destination')

def adminlogin(request):
    return render(request,'adminlogin.html')

def adlogin(request):
    username_a = request.POST.get('username')
    password_a = request.POST.get('password')
    if User.objects.filter(username__contains=username_a).exists():
        user = authenticate(username=username_a,password=password_a)
        if user is not None:
            login(request,user)
            print(user)
            return redirect('index')
        else:
            return render(request,'adminlogin.html',{'msg':"Sorry... Invalid username or password"})
    else:
        return redirect('adminlogin')