from django.urls import path
from .views import home_view, contact_view, detail_view, category_view, SearchView

urlpatterns = [
    path('', home_view, name='home'),
    path('contact/', contact_view, name='contact'),
    path('category/<int:category_id>/', category_view, name='category'),
    path('post/<slug:post>/', detail_view, name='post_detail'),
    path('search/', SearchView.as_view(), name='search')
]