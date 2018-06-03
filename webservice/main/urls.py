from django.urls import path, include
from . import  views

urlpatterns = [
    path('', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('charts/', views.charts, name='charts'),
    path('predect/', views.predect, name='predect'),
    path('save_predect/', views.save_predect, name='save_predect'),
    path('result/<id>', views.result, name='result')
]

#testing git branch develop