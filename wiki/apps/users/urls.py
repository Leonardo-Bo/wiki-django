from django.urls import path, include
from .views import UserRegisterView, RequestPage, delete_user_view, profile, change_password
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('users/register/', UserRegisterView.as_view(), name='register'), 
    path('users/request-sent/', RequestPage, name='request'), 
    path('users/', include('django.contrib.auth.urls')), 
    path('users/profile/', profile, name='profile'),
    path('users/update-password/', change_password, name='change_password'), 
    path('users/password-reset/', auth_views.PasswordResetView.as_view(template_name='users/password_reset.html'), name='password_reset'),
    path('users/password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'), name='password_reset_confirm'),
    path('users/password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'), name='password_reset_complete'),
    path('users/delete-account/', delete_user_view, name='delete_account'), 
]
