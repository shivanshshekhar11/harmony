from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('room/<str:id>/', views.room, name='room'),
    path('create_room/', views.createRoom, name='create_room'),
    path('update_room/<str:id>/', views.updateRoom, name='update_room'),
    path('delete_room/<str:id>/', views.deleteRoom, name='delete_room'),
]
