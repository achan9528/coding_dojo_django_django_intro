from django.urls import path
from . import views

app_name = "onlineLibrary"

urlpatterns = [
    path('', views.index, name="index"),
    path('login', views.login, name="login"),
    path('register', views.register, name="register"),
    path('books', views.userHomepage, name="books"),
    path('addFavoriteBook', views.addFavoriteBook, name="addFavoriteBook"),
    path('editFavoriteBook/<int:bookID>', views.editFavoriteBook, name="editFavoriteBook"),
    path('unfavorite/<int:bookID>', views.unfavorite, name="unfavorite"),
    path('favorite/<int:bookID>', views.favorite, name="favorite"),
    path('books/<int:bookID>', views.bookDetails, name="bookDetails"),
    path('deleteBook/<int:bookID>', views.deleteBook, name="deleteBook"),
    path('logout', views.logout, name="logout"),
]
