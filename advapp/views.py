from django.shortcuts import render
from django.http import HttpResponse
from .models import Rides
from .forms import Advregform

# Create your views here.
def index(request):
    rides= Rides.objects.all()
    context= {
        'rides' : rides
    }
    return render(request,'adventsites/index.html',context)

def details(request,pk):
    ride=Rides.objects.get(pk=pk)
    if request.method=='POST':
        form=Advregform(request.POST)
        if form.is_valid():
            appli=form.save(commit=False)
            appli.advent=ride
            appli.save()
    form=Advregform()
    context= {
        'ride' : ride,
        'form' : form
    }
    return render(request,'adventsites/details.html',context)
