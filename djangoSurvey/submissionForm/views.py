from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    return render(request,"index.html")

def result(request):
    print("Got Request................")
    print(request.POST)
    context = {
        "Name": request.POST['username'],
        "Dojo_Location": request.POST['dojo_location'],
        "Favorite_Language": request.POST['favorite_language'],
        "Comment": request.POST['comment'],
    }
    # return redirect("/result")
    return render(request,"result.html",context)

def process(request):
    request.session['name'] = request.POST['username']
    request.session['counter'] = 100
    return redirect("/success")

def success(request):
    return render(request,"success.html")