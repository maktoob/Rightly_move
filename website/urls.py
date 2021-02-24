from django.urls import path
from . import views
from .views import home

urlpatterns = [
    path('', views.home, name='home'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/tag/<slug:slug>/', views.post_tag, name='post_tag'),
    path('search/', views.search_result, name='search_result'),
    path('contact/', views.contact, name='contact'),
    path('success/', views.success, name='success'),
    path('<category>/', views.post_by_category, name='post_by_category'),
]