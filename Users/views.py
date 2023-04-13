from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .forms import ProfileForm
from .serializiers import UserSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view

#######User Profile
@login_required
def profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile has been updated!')
            return redirect('profile')
    else:
        form = ProfileForm(instance=request.user)
    return render(request, 'Users/profile.html', {'form': form})


####listAllUsers
def user_list(request):
    users = User.objects.all()
    return render(request, 'Users/user_list.html', {'users': users})

@api_view(['GET'])
def userlist(request):
    users = User.objects.all()
    serializer = UserSerializer(users,many=True)
    return Response(serializer.data)

####deleteUserProfile

def user_delete(request, username):
    user = get_object_or_404(User, username=username)
    user.delete()
    return redirect('user_list')
    
#######ModifyUserProfile
def edit_user(request, username):
    user = User.objects.get(username=username)
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('user_list')
    else:
        form = ProfileForm(instance=user)
    return render(request, 'Users/edit_user.html', {'form': form})


