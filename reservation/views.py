from django.shortcuts import redirect, render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .forms import ReservationForm
from .models import Field, Reservation
from .serializers import ReservationSerializer

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