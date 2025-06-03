from django.urls import path
from .views import register_view, login_view, logout_view,profile_view,edit_profile_view, change_password_view

urlpatterns = [
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('profile/', profile_view, name='profile'),
    path('edit-profile/', edit_profile_view, name='edit_profile'),
    path('change-password/', change_password_view, name='change_password')
]
