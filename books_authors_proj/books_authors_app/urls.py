from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('books',views.index),
    path('books/<int:bookId>', views.bookInformation),
    path('books/<int:bookId>/delete', views.bookDelete),
    path('authors',views.authors),
    path('authors/<int:authorId>',views.authorInformation),
    path('authors/<int:authorId>/delete',views.authorDelete),
    path('booksAdd',views.booksAdd),
    path('authorsAdd',views.authorsAdd),
    path('existingBooksAdd', views.existingBooksAdd),
    path('existingAuthorsAdd', views.existingAuthorsAdd),
]
