from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.db.models import Q
from .models import Room, Topic, Message
from .forms import RoomForm

# Create your views here.


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')

    context = {'username': '', 'register': False}

    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)

            if user is not None:
                user = authenticate(
                    request, username=username, password=password)

                if user is not None:
                    login(request, user)
                    return redirect('home')
                else:
                    messages.error(request, 'Password is incorrect')
                    context['username'] = username
        except:
            messages.error(request, 'User does not exist')

    return render(request, 'base/login_register.html', context)


def logoutPage(request):
    logout(request)
    return redirect('home')


def registerPage(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')

        else:
            messages.error(request, 'Form invalid')

    form = UserCreationForm()
    context = {'register': True, 'form': form}

    return render(request, 'base/login_register.html', context)


def userProfile(request, id):
    user = User.objects.get(id=id)
    rooms = user.room_set.all()
    messages = user.message_set.all()

    return render(request, 'base/user.html', {'rooms': rooms, 'room_messages': messages, 'user': user})


def home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''

    topics = Topic.objects.all()
    rooms = Room.objects.filter(Q(topic__name__icontains=q) | Q(name__icontains=q) | Q(
        host__username__icontains=q) | Q(description__icontains=q))
    messages = Message.objects.filter(Q(room__topic__name__icontains=q))

    return render(request, 'base/home.html', {'rooms': rooms, 'topics': topics, 'room_count': rooms.count(), 'room_messages': messages})


def room(request, id):
    room = Room.objects.get(id=id)

    if request.method == 'POST':
        message = Message.objects.create(
            author=request.user,
            room=room,
            body=request.POST.get('body')
        )
        room.participants.add(request.user)
        return redirect('room', id=room.id)

    roomMessages = room.message_set.all().order_by('-created_at')
    participants = room.participants.all()
    return render(request, 'base/room.html', {'room': room, 'room_messages': roomMessages, 'participants': participants})


@login_required(login_url='login')
def createRoom(request):
    form = RoomForm()

    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            room = form.save(commit=False)
            room.host = request.user
            room.save()
            return redirect('home')

    return render(request, 'base/room_form.html', {'form': form})


@login_required(login_url='login')
def updateRoom(request, id):
    room = Room.objects.get(id=id)
    form = RoomForm(instance=room)

    if room.host != request.user:
        return HttpResponse('Nope')

    if request.method == 'POST':
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('home')

    return render(request, 'base/room_form.html', {'form': form})


@login_required(login_url='login')
def deleteRoom(request, id):
    room = Room.objects.get(id=id)

    if room.host != request.user:
        return HttpResponse('Nope')

    if request.method == 'POST':
        room.delete()
        return redirect('home')

    return render(request, 'base/delete.html', {'obj': room})


@login_required(login_url='login')
def deleteMessage(request, id):
    message = Message.objects.get(id=id)

    if message.author != request.user:
        return HttpResponse('Nope')

    if request.method == 'POST':
        id = message.room.id
        message.delete()
        return redirect('room', id=id)

    return render(request, 'base/delete.html', {'obj': message})
