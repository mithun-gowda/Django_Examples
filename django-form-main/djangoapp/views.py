from django.shortcuts import render

# Create your views here.

from .forms import RegisterForm


def Registerview(request):
    form=RegisterForm()
    return render(request,'regform.html',{'form':form})