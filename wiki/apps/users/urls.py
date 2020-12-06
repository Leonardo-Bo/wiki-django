from django.urls import path
from .views import UserRegisterView, RequestPage, all_users, delete_user_view, profile, change_password
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('users/register/', UserRegisterView.as_view(), name='register'), 
    path('users/request-sent/', RequestPage, name='request'), 
    path('users/login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('users/logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('users/profile/<slug:slug>', profile, name='profile'),
    path('users/update-password/', change_password, name='change_password'), 
    path('users/password-reset/', auth_views.PasswordResetView.as_view(template_name='users/password_reset.html'), name='password_reset'),
    path('users/password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'), name='password_reset_confirm'),
    path('users/password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'), name='password_reset_complete'),
    path('users/delete-account/', delete_user_view, name='delete_account'), 
    path('users/user-list/', all_users, name='user_list'),
]
