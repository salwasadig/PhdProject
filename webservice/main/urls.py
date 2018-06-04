from django.urls import path, include
from . import  views

urlpatterns = [
    path('', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('charts/', views.charts, name='charts'),
    path('predect/', views.predect, name='predect'),
    path('savePredict/', views.savePredict, name='savePredict'),
    path('result/<id>', views.result, name='result'),
    path('myprojects/', views.myprojects, name='myprojects'),
    path('getProject/<id>', views.getProject, name='getProject'),
    path('updatePredict/<id>', views.updatePredict, name='updatePredict'),
]