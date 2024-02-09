from django.shortcuts import render
from django.http import HttpResponse
from app1.models import Product

# Create your views here.

def Productview(request,pn,br,pr):
    Product.objects.create(pname=pn,brand=br,price=pr)
    return HttpResponse("Data Has been Stored!")


    #here we don't have html page so we use HttpResponse method 
    #in this we get data from the user through url and store in mysql database