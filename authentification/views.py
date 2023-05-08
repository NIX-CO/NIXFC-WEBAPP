from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate, login,logout
from django.urls import reverse
from rest_framework.decorators import api_view
from django.http import JsonResponse

from .forms import CustomUserCreationForm
from .serializers import UserSerializer
# # Create your views here.

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Rediriger vers une page de confirmation ou de connexion
            return redirect('/')
    else:
        form = CustomUserCreationForm()
    return render(request, 'signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            error_message = 'Invalid username or password'
    else:
        error_message = ''
    return render(request, 'login.html', {'error_message': error_message})

def logout_view(request):
    logout(request)
    return redirect(reverse('home'))

@api_view(['POST'])
def signup_api(request):
    form = CustomUserCreationForm(request.POST)
    if form.is_valid():
        user = form.save()
        return JsonResponse({'success': True, 'message': 'User created successfully'})
    else:
        return JsonResponse({'success': False, 'errors': form.errors})

@api_view(['POST'])
def login_api(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return JsonResponse({'success': True, 'message': 'Login successful'})
    else:
        return JsonResponse({'success': False, 'message': 'Invalid username or password'})

@api_view(['POST'])
def logout_api(request):
    logout(request)
    return JsonResponse({'success': True, 'message': 'Logout successful'})