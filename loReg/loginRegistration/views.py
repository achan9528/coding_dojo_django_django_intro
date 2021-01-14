from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User
import bcrypt

# Create your views here.
def index(request):
    return render(request, "login.html")

def registerUser(request):
    errors = User.objects.validator(request.POST)

    if len(errors) > 0:
        for key,value in errors.items():
            messages.error(request,value)
        return redirect('/')
    else:
        firstName = request.POST['firstName']
        lastName = request.POST['lastName']
        email = request.POST['email']
        password = request.POST['password']
        passwordConfirm = request.POST['passwordConfirm']
        pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

        if len(User.objects.filter(email=email)) > 0:
            return redirect('/users/register/error/userExists')
        else:
            User.objects.create(
                firstName = firstName,
                lastName = lastName,
                email = email,
                password = pw_hash
            )
            request.session['firstName'] = firstName
            request.session['lastName'] = lastName
            return redirect('/success')
            

def errorPage(request, errorMessage):
    if errorMessage == "userExists":
        header = "Error - email already exists in system. Try another email!",
    if errorMessage == "incorrectPW":
        header = "Error - Password is incorrect. Try again!",
    context = {
            "header": header,
        }

    return render(request, "portal.html",context)

def login(request):
    users = User.objects.filter(email=request.POST['email'])
    if users:
        logged_user = users[0]
        if bcrypt.checkpw(request.POST['password'].encode(), logged_user.password.encode()):
            request.session['firstName'] = logged_user.firstName
            request.session['lastName'] = logged_user.lastName
            return redirect("/success")
        else:
            return redirect("/users/login/error/incorrectPW")

def success(request):
    context = {
        "header": f"Success! Welcome {request.session['firstName']}!",
        "header2": "Successfully registered (or logged in!)"
    }

    return render(request, "portal.html", context)

def logout(request):
    request.session.clear()
    return redirect('/')