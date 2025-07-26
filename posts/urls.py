from django.urls import path
from .views import post_list_view, post_detail_view, category_post_list_view

urlpatterns = [
    path('', post_list_view, name='post_list'),
    path('category/<slug:slug>/', category_post_list_view, name='category_post_list'),
    path('<slug:slug>/', post_detail_view, name='post_detail'),
]