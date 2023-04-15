from django.shortcuts import render, get_object_or_404, redirect
from .forms import MatchForm, MatchDeleteForm
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

def match_delete(request, pk):
    match = get_object_or_404(Match, pk=pk)
    if request.method == 'POST':
        form = MatchDeleteForm(request.POST)
        if form.is_valid():
            match.delete()
            return redirect('match_list')
    else:
        form = MatchDeleteForm()
    return render(request, 'match_delete.html', {'match': match, 'form': form})
def match_list(request):
    matches = Match.objects.all()
    context = {'matches': matches}
    return render(request, 'match_list.html', context)

def match_detail(request, pk):
    match = get_object_or_404(Match, pk=pk)
    if request.method == 'POST':
        form = MatchForm(request.POST, instance=match)
        if form.is_valid():
            form.save()
            return redirect('match:match_list')
    else:
        form = MatchForm(instance=match)
    context = {'match': match, 'form': form}
    return render(request, 'match_detail.html', context)  
def match_update(request, pk):
    match = get_object_or_404(Match, pk=pk)
    if request.method == 'POST':
        form = MatchForm(request.POST, instance=match)
        if form.is_valid():
            form.save()
            return redirect('match_list.html')
    else:
        form = MatchForm(instance=match)
    return render(request, 'match_update.html', {'form': form, 'match': match})    