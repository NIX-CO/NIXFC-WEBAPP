from django.shortcuts import render, redirect
from .forms import MatchForm
from .models import Match

def create_match(request):
    if request.method == 'POST':
        form = MatchForm(request.POST)
        if form.is_valid():
            match = form.save()
            return render(request, 'match_created.html', {'match': match})
    else:
        form = MatchForm()
    return render(request, 'create_match.html', {'form': form})
