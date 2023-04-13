from django.urls import path
from . import views

urlpatterns = [
    
    path('match/create/', views.create_match, name='create_match'),
]
