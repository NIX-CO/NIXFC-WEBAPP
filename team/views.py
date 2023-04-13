from django.shortcuts import render
from django.shortcuts import render,redirect,get_object_or_404
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


def team_update(request, pk):
    team = get_object_or_404(Team, pk=pk)
    if request.method == 'POST':
        form = TeamForm(request.POST, request.FILES, instance=team)
        if form.is_valid():
            form.save()
            return redirect('team_list')
    else:
        form = TeamForm(instance=team)
    return render(request, 'update_team.html', {'form': form})


