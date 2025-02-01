from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db.models import Q
from .models import Room, Topic
from .forms import RoomForm

# Create your views here.


def home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''

    topics = Topic.objects.all()
    rooms = Room.objects.filter(Q(topic__name__icontains=q) | Q(name__icontains=q) | Q(
        host__username__icontains=q) | Q(description__icontains=q))
    return render(request, 'base/home.html', {'rooms': rooms, 'topics': topics, 'room_count': rooms.count()})


def room(request, id):
    room = Room.objects.get(id=id)

    return render(request, 'base/room.html', {'room': room})


def createRoom(request):
    form = RoomForm()

    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    return render(request, 'base/room_form.html', {'form': form})


def updateRoom(request, id):
    room = Room.objects.get(id=id)
    form = RoomForm(instance=room)

    if request.method == 'POST':
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('home')

    return render(request, 'base/room_form.html', {'form': form})


def deleteRoom(request, id):
    room = Room.objects.get(id=id)

    if request.method == 'POST':
        room.delete()
        return redirect('home')

    return render(request, 'base/delete.html', {'obj': room})
