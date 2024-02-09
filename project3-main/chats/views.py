from django.shortcuts import render
from django.http import HttpResponse  #add this
# Create your views here.

#method 1

def register(request):
    with open(r'C:\Users\mithu\OneDrive\Desktop\jango\project3\chats\templates\register.html','r') as fp:
        data=fp.read()
        return HttpResponse(data)
        
# render process above one
#method 2


def login_view(request):
    return render(request,'register.html')

def sample(request):
    return HttpResponse('<h1>Hello Universe<h1>')