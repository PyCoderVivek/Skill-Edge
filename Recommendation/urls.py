# recommendation/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.recommendation_dashboard, name='recommendation_dashboard'),
]
