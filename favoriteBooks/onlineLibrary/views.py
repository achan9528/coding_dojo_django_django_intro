from django.shortcuts import render, redirect
from django.contrib import messages
from onlineLibrary.models import User, Book
import bcrypt

# Create your views here.
def index(request):
    return render(request, 'login.html')

def login(request):
    errors = User.objects.loginValidator(request.POST)
    users = User.objects.filter(email=request.POST['email'])
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request,value)
        return redirect('onlineLibrary:loginError')
    elif users:
        logged_user = users[0]
        if bcrypt.checkpw(request.POST['password'].encode(), logged_user.password.encode()):
            request.session['userID'] = logged_user.id
            return redirect('onlineLibrary:books')
    else:
        return redirect('onlineLibrary:loginError')

def loginError(request):
    context = {
        "errorComment": "Oh no! Something happened!"
    }
    return render(request, "login.html", context)

def register(request):
    errors = User.objects.registrationValidator(request.POST)
    if len(errors) > 0:
        for key,value in errors.items():
            messages.error(request, value)
        return redirect('onlineLibrary:registrationError')
    elif len(User.objects.filter(email=request.POST['email'])) > 0:
        return redirect('onlineLibrary:registrationError')
    else:
        password = request.POST['password']
        pwHash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
        newUser = User.objects.create(
            firstName = request.POST['firstName'],
            lastName = request.POST['lastName'],
            email = request.POST['email'],
            password = pwHash,
        )
        return render(request, "login.html")

def registrationError(request):
    context = {
        "errorMessage":"Oh no! Something happened!"
    }
    return render(request,"login.html",context)

def userHomepage(request):
    context = {
        "user": User.objects.get(id=request.session['userID']),
        "books": Book.objects.all(),
    }
    return render(request, "portal.html", context)

def addFavoriteBook(request):
    errors = Book.objects.creationManager(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('onlineLibrary:books')
    elif len(Book.objects.filter(title=request.POST['title'])) > 0:
        existingBook = Book.objects.get(title=request.POST['title'])
        User.object.get(request.session['user']).books_liked.add(existingBook)
        return redirect("onlineLibrary:bookDetails", bookID=existingBook.id)
    else:
        newBook = Book.objects.create(
            title=request.POST['title'],
            desc=request.POST['desc'],
            uploadedBy = User.objects.get(id=request.session['userID'])
        )
        User.objects.get(id=request.session['userID']).books_liked.add(newBook)
        return redirect("onlineLibrary:bookDetails", bookID=newBook.id)

def editFavoriteBook(request, bookID):
    errors = Book.objects.creationManager(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('onlineLibrary:books')
    else:
        existingBook = Book.objects.get(id=bookID)
        existingBook.title = request.POST['title']
        existingBook.desc = request.POST['desc']
        return redirect("onlineLibrary:bookDetails", bookID=newBook.id)

def unfavorite(request, bookID):
    loggedUser = User.objects.get(id=request.session['userID'])
    loggedUser.books_liked.remove(Book.objects.get(id=bookID))
    return redirect('onlineLibrary:books')

def favorite(request, bookID):
    loggedUser = User.objects.get(id=request.session['userID'])
    loggedUser.books_liked.add(Book.objects.get(id=bookID))
    return redirect('onlineLibrary:books')

def bookDetails(request, bookID):
    currentBook = Book.objects.get(id=bookID)
    loggedUser = User.objects.get(id=request.session['userID'])
    if currentBook.uploadedBy == loggedUser:
        templateContext = "user"
    else:
        templateContext = "viewer"
    
    context = {
        "templateContext" : templateContext,
        "book": currentBook,
        "loggedUser": loggedUser,
        "books": Book.objects.all(),
    }

    return render(request,"book.html", context)

def deleteBook(request, bookID):
    existingBook = Book.objects.get(id=bookID)
    existingBook.delete()
    return redirect('onlineLibrary:books')

def logout(request):
    request.session.clear()
    return redirect('onlineLibrary:index')