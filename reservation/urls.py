from django.urls import path
from . import views

app_name = 'reservations'

urlpatterns = [
    path('listeRsv/', views.liste_r, name='liste_r'),
    path('reserver/', views.reserver_terrain, name='reserver_terrain'),
]