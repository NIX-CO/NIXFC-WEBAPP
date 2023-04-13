from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Player
from .forms import PlayerForm

@login_required
def player_list(request):
    players = Player.objects.all()
    return render(request, 'player/player_list.html', {'players': players})

@login_required
def player_add(request):
    if request.method == 'POST':
        form = PlayerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('player_list')
    else:
        form = PlayerForm()
    return render(request, 'player/player_form.html', {'form': form})
