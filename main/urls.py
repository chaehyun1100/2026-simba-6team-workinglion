from django.urls import path
from . import views
from .views import *

app_name = 'main'

urlpatterns = [
    path('onboarding/', views.onboarding, name='onboarding'),
    path('signup_login/', views.signup_login, name='signup_login'),
]