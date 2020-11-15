from django.urls import path
from .views import Dashboard


urlpatterns = [
    path('dashboard/', Dashboard.as_view(), name='dashboard'),
]
