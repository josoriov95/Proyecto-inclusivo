from django.urls import path
from . import views

urlpatterns = [
    path('', views.root, name='login'),
    path('home', views.home, name='home'),
]
