from django.shortcuts import redirect, render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .forms import ReservationForm
from .models import Field, Reservation
from .serializers import ReservationSerializer

def reserver_terrain(request):
    message = ''
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.user = request.user
            reservation.save()
            message = 'message success'
            reservation_list = Reservation.objects.all()
            return render(request, 'ListReservation.html', {'form': form, 'reservation': reservation_list, 'message': message})
        else:
            message = 'Le formulaire n\'est pas valide. Veuillez réessayer.'
    else:
        form = ReservationForm()
    return render(request, 'reservation.html', {'form': form, 'message': message})



####listAllReservation
def liste_r(request):
    reservation_list = Reservation.objects.all()
    return render(request, 'ListReservation.html', {'reservation': reservation_list})