from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('books',views.index),
    path('books/<int:bookId>', views.bookInformation),
    path('authors',views.authors),
    path('authors/<int:authorId>',views.authorInformation),
    path('booksAdd',views.booksAdd),
    path('authorsAdd',views.authorsAdd),
    path('existingBooksAdd', views.authorsAdd),
    path('existinAuthorsAdd', views.authorsAdd),
]
