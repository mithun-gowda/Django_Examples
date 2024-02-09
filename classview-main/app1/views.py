from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from .forms import CartForm,Cart
# Create your views here.

#fucntion view
def Cartvw(request):
    form= CartForm()
    if request.method=='POST':
        form=CartForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("data stored")
    return render(request,'cart.html',{'form':form})



#class view
class Cartcview(View):
    def get(sef,request):
        form=CartForm()
        return render(request,'cart.html',{'form':form})

    def post(self,request):
        form=CartForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("data stored")

def Cartup(request,pk):
    data=Cart.objects.get(pid=pk)
    form=CartForm(instance=data)
    
    if request.method=='POST':
        form=CartForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("data stored")
    
    return render(request,'cartup.html',{'form':form})


class Cartcviewup(View):

    def get(self,request,pk):
        data=Cart.objects.get(pid=pk)
        form=CartForm(instance=data)
        return render(request,'cartup.html',{'form':form})

    def post(self,request,pk):
        data=Cart.objects.get(pid=pk)
        form=CartForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("data stored")
    
   