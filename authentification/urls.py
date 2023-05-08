from django.urls import path
from .views import signup,login_view,logout_view,signup_api,login_api,logout_api

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('api/signup/', signup_api, name='signup_api'),
    path('api/login/', login_api, name='login_api'),
    path('api/logout/', logout_api, name='logout_api'),
]   