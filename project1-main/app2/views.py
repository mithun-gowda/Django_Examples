from django.shortcuts import render

# Create your views here.
def sample1(request):
    return render(request,'sample1.html')

def sample(request):
    return render(request,'sample.html')