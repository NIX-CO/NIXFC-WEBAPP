from django.urls import path
from .views import field_list,create_field,delete_field

urlpatterns = [
    path('', field_list, name='field_list'),
    path('createfield/', create_field, name='createfield'),
    path('delete/', delete_field, name='deletefield'),


]
