from django.urls import path, include
from . import  views

urlpatterns = [
    path('', views.home, name='home'),
    path('dashboard/', views.home, name='home'),
    path('dashboardcharts/', views.dashboardcharts, name='dashboardcharts'),
    path('projectscharts/', views.projectscharts, name='projectscharts'),
    path('predect/', views.predect, name='predect'),
    path('savePredict/', views.savePredict, name='savePredict'),
    path('result/<id>', views.result, name='result'),
    path('myprojects/', views.myprojects, name='myprojects'),
    path('getProject/<id>', views.getProject, name='getProject'),
    path('updatePredict/<id>', views.updatePredict, name='updatePredict'),
]