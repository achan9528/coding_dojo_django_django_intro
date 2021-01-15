from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Comment, Message
from loginRegistration.models import User

# Create your views here.
def index(request):
    context = {
        "userFirstName": request.session["firstName"],
        "userLastName": request.session["lastName"],
        "userMessages": Message.objects.order_by("-created_at"),
        "userComments": Comment.objects.order_by("-created_at"),
    }
    return render(request,"wall.html", context)

def postMessage(request):
    
    errors = Message.objects.messageValidator(request.POST)

    if len(errors) > 0:
        for key,value in errors.items():
            messages.error(request,value)
        return redirect('dojoWall:postMessageError')
    else:
        messageText = request.POST['messageText']
        newMessage = Message.objects.create(
            message = messageText,
            user = User.objects.get(id=request.session['userID'])
        )
        return redirect('dojoWall:postMessageSuccess')

def postMessageError(request, errorMessage):
    context = {
        "errors": "Oh no! There was an error!",
    }

    return render(request,"wall.html", context)

def postMessageSuccess(request):
    return redirect('dojoWall:wall')

def postComment(request, messageID):
    
    errors = Comment.objects.commentValidator(request.POST)

    if len(errors) > 0:
        for request,value in errors.items():
            messages.error(request,value)
        return redirect('dojoWall:postCommentError', errorMessage="Comment Error!")
    else:
        comment = request.POST['comment']
        userID = request.session['userID']
        Comment.objects.create(
            comment = comment,
            user = User.objects.get(id=request.session['userID']),
            message = Message.objects.get(id=messageID)
        )
        return redirect('dojoWall:postCommentSuccess')

def postCommentError(request, errorMessage):
    context = {
        "errorMessage": errorMessage,
    }
    return render(request,"wall.html", context)

def postCommentSuccess(request):
    return redirect('dojoWall:wall')

def logout(request):
    request.session.clear()
    return redirect('loginRegistration:index')