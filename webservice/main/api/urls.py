from django.urls import path, include
from .views import  (
    ProjectAPICreateView,
    ProjectAPIDetailView,
    ProjectAPIListView,
    ProjectAPIUpdateView,
    ProjectAPIDeleteView
)

urlpatterns = [
    path('create', ProjectAPICreateView.as_view(), name='create-api'),
    path('<pk>', ProjectAPIDetailView.as_view(), name='details-api'),
    path('', ProjectAPIListView.as_view(), name='list-api'),
    path('<pk>/update/', ProjectAPIUpdateView.as_view(), name='update-api'),
    path('<pk>/delete/', ProjectAPIDeleteView.as_view(), name='delete-api'),
]