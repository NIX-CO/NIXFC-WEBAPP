from django.urls import path
from . import views

urlpatterns = [
    path('display/', views.player_list, name='player_list'),
    path('add/', views.player_add, name='player_add'),
    
]
