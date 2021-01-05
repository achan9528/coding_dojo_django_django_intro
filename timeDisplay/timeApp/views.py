from django.shortcuts import render, HttpResponse
import datetime

# Create your views here.
def index(request):
    now = datetime.datetime.now()
    context={
        "date": now.strftime("%m-%d-%Y"),
        "time": now.strftime("%H:%M"),
    }
    return render(request,'index.html',context)