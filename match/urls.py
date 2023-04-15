from django.urls import path
from . import views
from .views import match_delete , match_update , create_match ,match_detail , match_list


urlpatterns = [
    
    path('create/', create_match, name='create_match'),
    path('<int:pk>/delete/', match_delete, name='match_delete'),
    path('<int:pk>/update/', match_update, name='match_update'),
    path('', match_list, name='match_list'),
    
    path('<int:pk>', match_detail, name='match_detail'),



]
