from django.shortcuts import render, redirect
from .models import Field, Reservation
from .forms import ReservationForm

def reserver_terrain(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.user = request.user
            reservation.save()      
            return redirect('liste_r')
            # return render(request, 'ListReservation.html', {'form': form})
    else:
        form = ReservationForm()
    return render(request, 'reservation.html', {'form': form})



####listAllReservation
def liste_r(request):
    reservation = Reservation.objects.all()
    return render(request, 'ListReservation.html', {'reservation': reservation})

####DetailReservation
# def detail_r(request):
#     form = Reservation.objects.all()
#     return render(request, 'ListReservation.html', {'reservation': reservation})

