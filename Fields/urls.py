from django.urls import path
from .views import field_list,field_update,create_field,delete_field,FieldList,field_detail

urlpatterns = [
    path('', field_list, name='field_list'),
    path('<int:pk>/update/', field_update, name='field_update'),
    path('createfield/', create_field, name='createfield'),
    path('delete/', delete_field, name='deletefield'),
    path('field/<int:pk>/', field_detail, name='field-detail'),
    path('api/fields/', FieldList, name='api-fields'),
]
