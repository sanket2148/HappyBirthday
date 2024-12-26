from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
path('surprise/', views.surprise, name='surprise'),
path('login/', views.login_view, name='login'),
]
