from django.shortcuts import render, redirect, HttpResponse
import random

# Create your views here.
def index(request):
    if 'attempts' in request.session:
        message = request.session['message']
        attempts = request.session['attempts']
    else:
        random_number = random.randint(1,100)
        request.session['random_number'] = random_number
        message = ""
        attempts = 0

    context = {
        'message': message,
        'attempts': attempts,
    }

    print(request.session['random_number'])
    return render(request,"index.html", context)

def check(request):

    if 'attempts' in request.session:
        request.session['attempts'] = request.session['attempts'] + 1
    else:
        request.session['attempts'] = 1
    attempts = request.session['attempts']

    if int(request.POST['guess']) == request.session['random_number']:
        message = 'Good Guess! You got it right!'
    elif int(request.POST['guess']) > request.session['random_number']:
        message = 'Too High!'
    else:
        message = 'Too Low!'
    
    request.session['message'] = message
    request.session['attempts'] = attempts

    print(message)
    return redirect("/")

def delete_session(request):
    request.session.clear()
    return redirect("/")