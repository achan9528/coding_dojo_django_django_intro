from django.shortcuts import render, HttpResponse, redirect
from .models import Dojo, Ninja

# Create your views here.
def index(request):
    context = {
        "dojos": Dojo.objects.all(),
        "ninjas": Ninja.objects.all(),
    }
    return render(request, "index.html", context)

def addDojo(request):
    dojoName = request.POST['addDojoName']
    dojoCity = request.POST['addDojoCity']
    dojoState = request.POST['addDojoState']
    Dojo.objects.create(name = dojoName, city= dojoCity, state=dojoState)
    return redirect('/')

def addNinja(request):
    ninjaFirstnName = request.POST['addNinjaFirstName']
    ninjaLastName = request.POST['addNinjaLastName']
    ninjaDojo = request.POST['selectDojo']
    Ninja.objects.create(dojo = Dojo.objects.get(name=ninjaDojo), first_name=ninjaFirstnName, last_name=ninjaLastName)
    return redirect('/')