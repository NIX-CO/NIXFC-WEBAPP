from django.urls import path
from . import views

app_name = 'reservations'

urlpatterns = [
    path('listeRsv/', views.liste_r, name='liste_r'),
    path('reserver/', views.reserver_terrain, name='reserver_terrain'),
    path('api/reserve/', views.reserver_terrain_api, name='reserver_terrain_api'),
    path('api/list-reservations/', views.liste_r_api, name='liste_r_api'),
]