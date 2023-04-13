from django.shortcuts import render, redirect
from .forms import RoomForm, AddUserForm, AddUserToRoomForm
from .models import Room
from django.shortcuts import render, redirect, get_object_or_404


def create_room(request):
    form = RoomForm(request.POST or None)
    if form.is_valid():
        room = form.save(commit=False)
        room.user = request.user
        room.save()
        form.save_m2m()
        return redirect('add_user', room_id=room.id)
    context = {'form': form}
    return render(request, 'create_room.html', context)

def add_user(request, room_id):
    room = get_object_or_404(Room, id=room_id)
    form = AddUserToRoomForm(request.POST or None, room=room)

    if form.is_valid():
        users = form.cleaned_data.get('users')
        for user in users:
            room.users_list.add(user)

    context = {'room': room, 'form': form}
    return render(request, 'add_user.html', context)
def room_detail(request, room_id):
    room = get_object_or_404(Room, id=room_id)
    context = {'room': room}
    return render(request, 'room_detail.html', context)

def room_edit(request, room_id):
    room = get_object_or_404(Room, id=room_id)
    form = RoomForm(request.POST or None, instance=room)
    if form.is_valid():
        form.save()
        return redirect('room_detail', room_id=room.id)
    context = {'form': form, 'room': room}
    return render(request, 'room_edit.html', context)

def room_delete(request, room_id):
    room = get_object_or_404(Room, id=room_id)
    if request.method == 'POST':
        room.delete()
        return redirect('create_room')
    context = {'room': room}
    return render(request, 'room_delete.html', context)    
def room_list(request):
    rooms = Room.objects.all()
    return render(request, 'room_list.html', {'rooms': rooms})