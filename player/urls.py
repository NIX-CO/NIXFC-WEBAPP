from django.urls import path
from . import views

urlpatterns = [
   
    path('add/', views.player_add, name='player_add'),
    
]