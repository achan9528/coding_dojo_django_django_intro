from django.urls import path, include
from . import views

app_name = "loginRegistration"

urlpatterns = [
    path('', views.index, name="index"),
    path('users/register', views.registerUser, name="registerUser"),
    path('users/register/error/<str:errorMessage>', views.errorPage, name="raiseRegisterError"),
    path('users/login', views.login, name="loginUser"),
    path('users/login/error/<str:errorMessage>', views.errorPage, name="raiseLoginError"),
    path('success', views.success, name="loginSuccess"),
    path('logout', views.logout, name="logout"),
]

