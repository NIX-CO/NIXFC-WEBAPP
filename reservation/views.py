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


@api_view(['POST'])
def reserver_terrain_api(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.user = request.user
            reservation.save()
            return Response({'success': True, 'message': 'Reservation created successfully'})
        else:
            return Response({'success': False, 'errors': form.errors})

@api_view(['GET'])
def liste_r_api(request):
    reservations = Reservation.objects.all()
    serializer = ReservationSerializer(reservations, many=True)
    return Response(serializer.data)