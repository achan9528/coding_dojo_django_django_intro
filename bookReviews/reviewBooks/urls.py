from . import views
from django.urls import path, include

app_name = "reviewBooks"

urlpatterns = [
    path('', views.index, name="index"),
    path('register', views.register, name="register"),
    path('register/error', views.registrationError, name="registrationError"),
    path('login', views.login, name="login"),
    path('login/error', views.loginError, name="loginError"),
    path('books', views.portal, name="portal"),
    path('books/add', views.addBookReview, name="addBookReview"),
    path('books/add/reviewNewBook', views.reviewNewBook, name="reviewNewBook"),
    path('books/<int:bookID>', views.bookDescription, name="bookDescription"),
    path('books/<int:bookID>/deleteReview/<int:reviewID>', views.deleteReview, name="deleteReview"),
    path('books/<int:bookID>/addReview', views.addReview, name="addReview"),
    path('user/<int:userID>', views.userDescription, name="userDescription"),
    path('logout', views.logout, name="logout"),
]