from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    path('login/', auth_views.LoginView.as_view(
        template_name='users/registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(
        template_name='users/registration/logout.html'), name='logout'),
    path('password-change/', auth_views.PasswordChangeView.as_view(
        template_name='users/registration/password_change_form.html'), 
         name='password_change'),
    path('password-change/done/', auth_views.PasswordChangeDoneView.as_view(
        template_name='users/registration/password_change_done.html'),
         name='password_change_done'),
]
