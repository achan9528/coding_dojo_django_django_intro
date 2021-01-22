from django.shortcuts import render, redirect
from .models import User, Book, Author, Review
from django.contrib import messages
import bcrypt

# Create your views here.
def index(request):
    return render(request, "login.html")

def register(request):
    errors = User.objects.registrationValidator(request.POST)
    if len(errors) > 0:
        for key,value in errors.items():
            messages.error(request, value)
        return redirect("reviewBooks:registrationError")
    else:
        password = request.POST['password']
        pwHash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
        newUser = User.objects.create(
            name=request.POST["name"],
            alias=request.POST["alias"],
            email=request.POST["email"],
            password=pwHash
        )
        request.session["userID"] = newUser.id
        return redirect("reviewBooks:portal")

def registrationError(request):
    return render(request, "login.html")

def login(request):
    errors = User.objects.loginValidator(request.POST)
    users = User.objects.filter(email=request.POST['email'])
    if len(errors) > 0:
        for key,value in errors.items():
            messages.error(request, value)
        return redirect ("reviewBooks:loginError")
    elif users:
        logged_user = users[0]
        if bcrypt.checkpw(request.POST['password'].encode(), logged_user.password.encode()):
            request.session['userID'] = logged_user.id
            return redirect("reviewBooks:portal")
        else:
            messages.error(request,"Password does not match!")
            return redirect("reviewBooks:loginError")
        

def loginError(request):
    return render(request,"login.html")

def portal(request):
    loggedUser = User.objects.get(id=request.session["userID"])
    books = Book.objects.all()
    reviews = Review.objects.order_by("-createdAt")[:3]
    context = {
        "user": loggedUser,
        "books": books,
        "reviews": reviews,
    }
    return render(request, "portal.html", context)

def bookDescription(request, bookID):
    currentBook = Book.objects.get(id=bookID)
    loggedUser = User.objects.get(id=request.session["userID"])
    context = {
        "book": currentBook,
        "user": loggedUser,
    }
    return render(request,"book.html", context)

def deleteReview(request, bookID, reviewID):
    Review.objects.get(id=reviewID).delete()
    return redirect("reviewBooks:books", bookID=bookID)

def addBookReview(request):
    context ={
        "authors": Author.objects.all(),
    }
    return render(request,"addBook.html", context)

def reviewNewBook(request):
    if request.POST["authorType"] == "":
        author = Author.objects.get(name=request.POST["authorDropdown"])
    else:
        author = Author.objects.create(
            name = request.POST["authorType"],
            addedBy = User.objects.get(id=request.session["userID"]),
        )
    newBook = Book.objects.create(
        title=request.POST['title'],
        author=author,
        addedBy = User.objects.get(id=request.session["userID"]),
    )
    newReview = Review.objects.create(
        comments = request.POST['reviewText'],
        creator = User.objects.get(id=request.session["userID"]),
        book = newBook,
        stars = request.POST["rating"],
    )

    return redirect("reviewBooks:portal")

def addReview(request, bookID):
    book = Book.objects.get(id=bookID)
    Review.objects.create(
        comments = request.POST['comments'],
        creator = User.objects.get(id=request.session['userID']),
        book = book,
        stars = request.POST["rating"],
    )
    
    return redirect("reviewBooks:portal")

def userDescription(request, userID):
    lookedUp = User.objects.get(id=userID)
    context = {
        "user":lookedUp,
    }
    return render(request,"user.html", context)

def logout(request):
    request.session.clear()
    return redirect("reviewBooks:index")