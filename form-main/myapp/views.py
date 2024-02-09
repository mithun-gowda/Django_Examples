from django.shortcuts import render
from myapp.models import Person
from myapp.models import Automobile
from django.http import HttpResponse
# Create your views here.

def Index(request):
    print(request)
    return render(request,'register.html')


def App(request):
    # print('App:-',request.GET)

    uname=request.GET['uname']
    email=request.GET['email']
    ph=request.GET['ph']
    Person.objects.create(username=uname,email=email,phone=ph)
    return render(request,'app.html',{'uname':uname,'email':email,'ph':ph})


def Autoview(request):
    if request.method == 'POST':
        type=request.POST['type']  # it is one method to request
        vname=request.POST.get('vname') # another method but both are same
        cname=request.POST['cname']
        year=request.POST['year']
        price=request.POST['price']
        Automobile.objects.create(type=type,vname=vname,cname=cname,year=year,price=price)
        return HttpResponse("Data is Stored")
    return render(request,'automobile.html')

def Autoread(request):
    data=Automobile.objects.all()
    return render(request,'readauto.html',{'data':data})

def Read_one(request,pk):
    data=Automobile.objects.get(id=pk)
    return render(request,'readone.html',{'data':data})

def Auto_update(request,pk):
    data=Automobile.objects.get(id=pk)
    if request.method == 'POST':
        type=request.POST['type']  
        vname=request.POST.get('vname')
        cname=request.POST['cname']
        year=request.POST['year']
        price=request.POST['price']
        Automobile.objects.filter(id=pk).update(type=type,vname=vname,cname=cname,year=year,price=price)
        return HttpResponse("Data is Updated")
    return render(request,'readupdate.html',{data:data})

def Auto_delete(request,pk):
    data=Automobile.objects.get()
    if request.method == 'POST':
        data=Automobile.objects.get().delete()
        return HttpResponse("Data has been deleted")
    return render(request,'delete.html',{data:data})