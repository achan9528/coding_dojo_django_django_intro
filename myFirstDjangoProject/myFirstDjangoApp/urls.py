from django.urls import path     
from . import views

urlpatterns = [
    path('', views.root),
    path('blog',views.index),
    path('blog/new',views.new),
    path('blog/create',views.create),
    path('blogs/<int:number>',views.show),
    path('blogs/<int:number>/edit',views.edit),
    path('blogs/<int:number>/delete',views.delete),
    path('blog/json',views.json),
]