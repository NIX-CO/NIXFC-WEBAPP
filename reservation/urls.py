from django.urls import path
from . import views

app_name = 'reservations'

urlpatterns = [
    path('reserve/', views.reserve_terrain, name='reserve_terrain'),
]