from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.
def index(request):
    request.session['view_count'] = request.session.get('view_count',0) + 1
    view_count = request.session['view_count']
    context = {
        "count": view_count,
    }
    print(context)
    return render(request,"index.html",context)

def delete(request):
    request.session.clear()
    if ('view_count' in request.session):
        return HttpResponse("Uh oh, delete unsuccessful!")
    else:
        return redirect('/')    