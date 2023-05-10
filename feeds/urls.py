from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:post_id>/', views.post_detail, name='post_detail'),
    path('create/', views.create_post, name='create_post'),
    path('api/posts/', views.PostListAPIView.as_view(), name='post_list_api'),
    path('api/posts/<int:post_id>/', views.PostDetailAPIView.as_view(), name='post_detail_api'),
    path('api/posts/create/', views.CreatePostAPIView.as_view(), name='create_post_api'),
    
]
