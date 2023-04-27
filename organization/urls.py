from django.urls import path
from .views import organization_list,organization_create,organization_update,organization_delete,organization_detail

app_name = 'organization'

urlpatterns = [
    # List organizations
    path('', organization_list, name='organization_list'),

    # Create organization
    path('create/', organization_create, name='organization_create'),

    # Update organization
    path('<int:pk>/update/', organization_update, name='organization_update'),

    # Delete organization
    path('<int:pk>/delete/', organization_delete, name='organization_delete'),

    path('<int:pk>/', organization_detail, name='organization_detail'),
]
