from django.urls import path
from . import views

urlpatterns = [
    path('manage/', views.manage_performance, name='manage_performance'),
]
