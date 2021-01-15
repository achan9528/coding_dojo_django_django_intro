from django.urls import path, include
from . import views

app_name = "dojoWall"

urlpatterns = [
    path('', views.index, name="index"),
    path('wall', views.index, name="wall"),
    path('wall/postMessage', views.postMessage, name="postMessage"),
    path('wall/postMessage/error/<str:errorMesssage>', views.postMessageError, name="postMessageError"),
    path('wall/postMessage/success', views.postMessageSuccess, name="postMessageSuccess"),
    path('wall/postComment/<int:messageID>', views.postComment, name="postComment"),
    path('wall/postComment/error/<str:errorMessage>', views.postCommentError, name="postCommentError"),
    path('wall/postComment/success', views.postCommentSuccess, name="postCommentSuccess"),
    path('wall/logout', views.logout, name="logout"),
]
