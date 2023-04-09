from django.urls import path
from . import views

urlpatterns = [
    path('register', views.registerView, name='Register'),
    path('login', views.loginView, name='Login'),
    path('logout', views.logoutView, name='Logout'),
]
