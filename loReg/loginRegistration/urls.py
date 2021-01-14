from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index),
    path('users/register', views.registerUser),
    path('users/register/error/<str:errorMessage>', views.errorPage),
    path('users/login', views.login),
    path('users/login/error/<str:errorMessage>', views.errorPage),
    path('success', views.success),
    path('logout', views.logout),
]

