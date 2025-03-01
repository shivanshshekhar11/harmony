from django.urls import path
from . import views

urlpatterns = [
    path('', views.getAllRoutes),
    path('rooms/', views.getAllRooms)
]
