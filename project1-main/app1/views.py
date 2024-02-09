from django.shortcuts import render

# Create your views here.

def register(request):
    return render(request,'register.html',{'name':'*Enter Valid Input'})

def user(request,pk):
    return render(request,'user.html',{'pk':pk})

def person(request):
    data=[{'Name':'Mithun','Age':23,'Phone':7259726975,'Address':'Bangalore'},
          {'Name':'Rocky','Age':25,'Phone':7233626975,'Address':'Mangalore'}]
    s='Mithun Gowda'
    return render(request,'details.html',{'data':data,'s':s})

def student(request):
    data1=[{'name':'Mithun','kan':98,'Eng':'Absent','phy':68,'che':50,'mat':45,'bio':49},
            {'name':'Sanvi','kan':48,'Eng':78,'phy':64,'che':79,'mat':38,'bio':78},
            {'name':'Sooraj','kan':58,'Eng':56,'phy':48,'che':68,'mat':65,'bio':69},
            {'name':'Rajesh','kan':97,'Eng':'92','phy':78,'che':98,'mat':85,'bio':89}
            ]
    return render(request,'student.html',{'data1':data1})