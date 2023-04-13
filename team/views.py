from django.shortcuts import render
from .forms import TeamForm
from .models import Team

def add_team(request):
    if request.method == 'POST':
        form = TeamForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request, 'success.html')
    else:
        form = TeamForm()
    return render(request, 'add_team.html', {'form': form})

def team_list(request):
    teams = Team.objects.all()
    return render(request, 'team_list.html', {'teams': teams})

