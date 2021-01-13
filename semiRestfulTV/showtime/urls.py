from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('shows',views.index),
    path('shows/new',views.addShowForm),
    path('shows/create',views.addShow),
    path('shows/<int:showID>', views.displayInfo),
    path('shows/<int:showID>/edit', views.editShowForm),
    path('shows/<int:showID>/update', views.editShow),
    path('shows/<int:showID>/destroy', views.destroy),
]
