from django.urls import path, include
from . import  views

urlpatterns = [
    path('', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('charts/', views.charts, name='charts')
]

#testing git branch develop