# from django.shortcuts import render
# from django.contrib.auth.forms import UserCreationForm


# # Create your views here.

# def signup(request):
   
#    form = UserCreationForm()
#    return render(request,'signup.html',{'form':form})

from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm

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