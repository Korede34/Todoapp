from django.urls import path
from . import  views

urlpatterns = [
    path('', views.index, name='home'),
    path('edit/<contact_id>/', views.edit, name='edit'),
    path('profile/<profile_id>/', views.profile, name='profile'),
    path('create', views.addcontact, name='create'),
    path('delete/<contact_id>/', views.deletecontact, name='delete'),
]
