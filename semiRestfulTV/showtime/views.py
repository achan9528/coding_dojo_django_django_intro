from django.shortcuts import render, redirect
from .models import Show, Network

# Create your views here.
def index(request):
    context = {
        "shows": Show.objects.all()
    }

    return render(request, "index.html", context)

def displayInfo(request, showID):
    requestedShow = Show.objects.get(id=showID)
    labels = ["Title", "Networks", "Release Date", "Description"]
    context = {
        "show": requestedShow,
    }

    return render(request, "displayInfo.html", context)

def addShowForm(request):
    
    context = {
        "header": "Add a New Show",
        "value_title": "",
        "value_network": "",
        "value_releaseDate": "",
        "value_desc": "",
        "buttonText": "Create",
        "formAction": "/shows/create",
    }
    
    return render(request, 'form.html', context)
    return render(request, "form.html")

def addShow(request):

    title = request.POST['title']
    network = request.POST['network']
    releaseDate = request.POST['releaseDate']
    desc = request.POST['desc']
    
    newShow = Show.objects.create(title=title, releaseDate= releaseDate, desc=desc)

    if Network.objects.filter(name=network).exists():
        networkObj = Network.objects.get(name=network)
        newShow.networks.add(networkObj)
    else:
        networkObj = Network.objects.create(name=network)
        newShow.networks.add(networkObj)

    return redirect(f"/shows/{newShow.id}")

def editShowForm(request, showID):

    currentShow = Show.objects.get(id=showID)
    print(currentShow.title)
    print(currentShow.networks.first().name)
    context = {
        "header": f"Edit Show {showID}",
        "show": currentShow,
        "value_title": currentShow.title,
        "value_network": currentShow.networks.first().name,
        "value_releaseDate": currentShow.releaseDate,
        "value_desc": currentShow.desc,
        "buttonText": "Update",
        "formAction": f"/shows/{showID}/update",
    }
    
    return render(request, 'form.html', context)

def editShow(request, showID):

    title = request.POST['title']
    network = request.POST['network']
    releaseDate = request.POST['releaseDate']
    desc = request.POST['desc']

    showToUpdate = Show.objects.get(id=showID)
    showToUpdate.title = title
    showToUpdate.network = network
    showToUpdate.releaseDate = releaseDate
    showToUpdate.desc = desc

    showToUpdate.save()

    return redirect(f"/shows/{showID}")

def destroy(request, showID):
    Show.objects.get(id=showID).delete()
    return redirect('/')