from django.shortcuts import render
from .forms import TrainerForm
from django.http import HttpResponse
from .models import TrainerModel
# Create your views here.

def TrainerView(request):
    form=TrainerForm()
    if request.method=='POST':
        form=TrainerForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Data has been Stored')
    return render(request,'trainerpro.html',{'form':form})


def TrainerUp(request,pk):
    data=TrainerModel.objects.get(empid=pk)
    form=TrainerForm(instance=data)
    if request.method == 'POST':
        form=TrainerForm(request.POST,instance=data)   #if instance is not mentioned it will create new record so instance should given
        if form.is_valid():
            form.save()
            return HttpResponse("DATA")
    return render(request,'trainerupdate.html',{'form':form})