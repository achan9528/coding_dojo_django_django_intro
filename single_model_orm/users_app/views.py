from django.shortcuts import render, redirect
from .models import User

# Create your views here.
def index(request):
    context = {
        "welcome_message": "hello!",
        "users": User.objects.all(),
    }
    return render(request, "index.html", context)

def processForm(request):
    User.objects.create(
        first_name = request.POST['firstName'],
        last_name = request.POST['lastName'],
        email_address = request.POST['emailAddress'],
        age = request.POST['age'],
    )
    return redirect('/')