from django.urls import path
from .views import field_list

urlpatterns = [
    path('', field_list, name='field_list'),
]
