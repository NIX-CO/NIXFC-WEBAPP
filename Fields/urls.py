from . import views
from django.urls import path
from .views import field_list,field_update,create_field,delete_field,FieldList,field_detail,my_reservation

urlpatterns = [
    path('', field_list, name='field_list'),
    path('<int:pk>/update/', field_update, name='field_update'),
    path('create/', create_field, name='createfield'),
    path('delete/', delete_field, name='deletefield'),
    path('<int:pk>/', field_detail, name='field-detail'),
    path('api/fields/', FieldList, name='api-fields'),
    path('search/', views.search, name='search'),
    path('show_reserved_fields/', views.show_reserved_fields, name='show_reserved_fields'),
    path('my_reservation/', views.my_reservation, name='my_reservation'),
    path('api/search/', views.SearchAPIView.as_view(), name='search'),
    path('api/reserved-fields/', views.show_reserved_fields, name='reserved-fields'),
    path('api/my-reservation/', views.my_reservation, name='my-reservation'),
]
