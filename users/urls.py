from django.urls import path
from .views import register_view, login_view, logout_view,profile_view,edit_profile_view, change_password_view, password_reset_request, password_reset_done_view, password_reset_confirm_view, password_reset_complete_view

urlpatterns = [
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('profile/', profile_view, name='profile'),
    path('edit-profile/', edit_profile_view, name='edit_profile'),
    path('change-password/', change_password_view, name='change_password'),
    path('password-reset/', password_reset_request, name='password_reset'),
    path('password-reset/done/', password_reset_done_view, name='password_reset_done'),
    path('reset/<uidb64>/<token>/', password_reset_confirm_view, name='password_reset_confirm'),
    path('reset/done/', password_reset_complete_view, name='password_reset_complete'),
]
