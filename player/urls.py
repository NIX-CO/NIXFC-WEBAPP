from django.urls import path
from . import views

urlpatterns = [
    path('display/', views.player_list, name='player_list'),
    path('add/', views.player_add, name='player_add'),
    path('update/<int:pk>/', views.player_update, name='player_update'),
]
