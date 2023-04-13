from django.urls import path
from .views import create_room, add_user, room_detail, room_edit, room_delete, room_list


urlpatterns = [
    path('create/', create_room, name='create_room'),
    path('add-user/<int:room_id>/',add_user, name='add_user'),
    path('room/<int:room_id>/', room_detail, name='room_detail'),
    path('room/<int:room_id>/edit/', room_edit, name='room_edit'),
    path('room/<int:room_id>/delete/', room_delete, name='room_delete'),
    path('', room_list, name='room_list'),
]