from django.urls import path
from .views import profile,user_list,user_delete,edit_user,userlist
from . import views

urlpatterns = [
    path('profile/', profile, name='profile'),
    path('user_list/', user_list, name='user_list'),
    path('delete/<str:username>/', user_delete, name='user_delete'),
    path('edit_user/<str:username>/', edit_user, name='edit_user'),
    path('api/users/', userlist, name='api-users'),
]
