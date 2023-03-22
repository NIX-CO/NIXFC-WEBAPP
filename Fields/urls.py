from django.urls import path
from . import views

urlpatterns = [
    path('createfield/', views.create_field, name='createfield'),

]