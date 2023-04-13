from django.urls import path
from . import views
from .views import match_delete


urlpatterns = [
    
    path('match/create/', views.create_match, name='create_match'),
    path('match/<int:pk>/delete/', match_delete, name='match_delete'),


]
