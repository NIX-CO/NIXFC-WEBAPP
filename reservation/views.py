from django.shortcuts import render, redirect
from .forms import ReservationForm

def reserve_terrain(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.user = request.user
            reservation.save()      
            return render(request, 'ListReservation.html', {'form': form})
    else:
        form = ReservationForm()
    return render(request, 'reservation.html', {'form': form})

