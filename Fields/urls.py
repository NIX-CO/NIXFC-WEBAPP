from django.urls import path
from .views import field_list,field_update

urlpatterns = [
    path('', field_list, name='field_list'),
    path('<int:pk>/update/', field_update, name='field_update'),
]
