from django.urls import path

from .views import *

app_name = 'main'

urlpatterns = [
    path('onboarding/', views.onboarding, name='onboarding'),
    path('signup_login/', views.signup_login, name='signup_login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('create_pot/', views.create_pot, name='create_pot'),
    path('join_pot/', views.join_pot, name='join_pot'),
]