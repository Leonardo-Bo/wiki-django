from django.urls import path, include
from .views import UserRegisterView, RequestPage, profile, change_password


urlpatterns = [
    path('users/register/', UserRegisterView.as_view(), name='register'), 
    path('users/request-sent/', RequestPage, name='request'), 
    path('users/', include('django.contrib.auth.urls')), 
    path('users/profile/', profile, name='profile'),
    path('users/update-password/', change_password, name='change_password'), 
]
