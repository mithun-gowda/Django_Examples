from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.
def appview(request):
    return HttpResponse('This is App3 Urls')