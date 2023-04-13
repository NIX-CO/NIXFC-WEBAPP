from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_team, name='add_team'),
    path('', views.team_list, name='team_list'),
]