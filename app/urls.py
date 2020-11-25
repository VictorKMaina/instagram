from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('accounts/register/', views.signup, name = 'register'),
    path('activate/<uid>/<token>/', views.activate, name='activation'),
    path('accounts/confirm-email/', views.confirm_email, name='confirm_email'),
    path('images/like/', views.add_like, name = 'add_like'),
    path('images/comment/', views.add_comment, name = 'add_comment')
]
