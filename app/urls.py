from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('accounts/register/', views.signup, name = 'register'),
    path('accounts/activate/', views.activate, name='activate')
]
