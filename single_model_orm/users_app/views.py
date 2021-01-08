from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        "welcome_message": "hello!"
    }
    return render(request, "index.html", context)