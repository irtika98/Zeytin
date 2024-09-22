from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('chat', views.chat, name='chat'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('logout', views.logout, name='logout'),
]