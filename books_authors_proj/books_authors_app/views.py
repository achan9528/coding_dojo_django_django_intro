from django.shortcuts import render, redirect
from .models import Book, Author

# Create your views here.
def index(request):
    labels = zip(["Title", "Description"],["addTitle", "addDescription"])
    tableHeaders = ["ID", "Title", "Action", "Delete"]
    context = {
        "subject": "books",
        "formHeader": "Add a Book",
        "labels": labels,
        "iterable": Book.objects.all(),
        "tableHeaders": tableHeaders,
    }
    
    return render(request,"index.html",context)

def authors(request):
    labels=zip(["First Name", "Last Name", "Notes"], ["addFirstName","addLastName","addNotes"])
    tableHeaders = ["ID", "First Name", "Last Name", "Action", "Delete"]
    context = {
        "subject": "authors",
        "formHeader": "Add an Author",
        "labels": labels,
        "iterable": Author.objects.all(),
        "tableHeaders": tableHeaders,
    }
    
    return render(request,"index.html",context)

def bookInformation(request, bookId):
    requestedBook = Book.objects.get(id=bookId)
    iterable=[]
    for author in requestedBook.authors.all():
        name = f"{author.first_name} {author.last_name}"
        iterable.append(name)

    iterable2 = []
    for author in Author.objects.all():
        name = f"{author.first_name} {author.last_name}"
        if name not in iterable:
            iterable2.append(name)
    if len(iterable2) == 0:
        iterable2.append("No authors left to add!")

    context = {
        "field0": "ID",
        "field1": "Description",
        "field2": "Authors",
        "header": requestedBook.title,
        "iterable": iterable,
        "options": iterable2,
        "formAction": "/existingAuthorsAdd",
        "requestedObject": requestedBook,
    }

    return render(request, "infoDisplay.html", context)

def authorInformation(request, authorId):
    requestedAuthor = Author.objects.get(id=authorId)
    iterable=[]
    for book in requestedAuthor.books.all():
        name = book.title
        iterable.append(name)

    iterable2=[]
    for book in Book.objects.all():
        name = book.title
        if name not in iterable:
            iterable2.append(name)
    if len(iterable2) == 0:
        iterable2.append("No books left to add!")

    context = {
        "field0": "ID",
        "field1": "Notes",
        "field2": "Books",
        "header": f"{requestedAuthor.first_name} {requestedAuthor.last_name}",
        "iterable": iterable,
        "options": iterable2,
        "formAction": "/existingBooksAdd",
        "requestedObject": requestedAuthor,
    }

    return render(request, "infoDisplay.html", context)

def booksAdd(request):
    title = request.POST['addTitle']
    desc = request.POST['addDescription']
    Book.objects.create(title=title,desc=desc)
    return redirect("/")

def authorsAdd(request):
    first_name = request.POST['addFirstName']
    last_name = request.POST['addLastName']
    notes = request.POST['addNotes']
    Author.objects.create(first_name=first_name,last_name=last_name,notes=notes)
    return redirect("/")

def existingBooksAdd(request):
    name = request.POST['topic'].split()
    currentAuthor = Author.objects.get(first_name = name[0], last_name = name[1])
    bookToAdd = Book.objects.get(title=request.POST['selection'])
    currentAuthor.books.add(bookToAdd)

    return redirect('/authors')

def existingAuthorsAdd(request):
    title = request.POST['topic']
    currentBook = Book.objects.get(title=title)
    name = request.POST['selection'].split()
    authorToAdd = Author.objects.get(first_name=name[0],last_name=name[1])
    currentBook.authors.add(authorToAdd)

    return redirect('/')

def bookDelete(request, bookId):
    Book.objects.get(id=bookId).delete()
    return redirect('/')

def authorDelete(request, authorId):
    Author.objects.get(id=authorId).delete()
    return redirect('/authors')