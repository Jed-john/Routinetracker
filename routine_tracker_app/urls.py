
from django.urls import path
from . import views
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('',views.home, name='home'),
    path('getstarted/', views.get_started, name='getstarted'),
    path('continue/', views.onboarding, name='onboarding'),

    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('myhome/', views.myhome,name='myhome'),
    
    
]